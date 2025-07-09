import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os

st.set_page_config(page_title="LocalBiz Insights", layout="wide")

USER_FILE = "users.csv"

# -----------------------------
# 🔐 Load or Create User Store
# -----------------------------
if not os.path.exists(USER_FILE):
    pd.DataFrame(columns=["username", "password", "business_name"]).to_csv(USER_FILE, index=False)

def load_users():
    return pd.read_csv(USER_FILE)

def save_user(username, password, business_name):
    users = load_users()
    if username in users['username'].values:
        return False  # already exists
    users.loc[len(users)] = [username, password, business_name]
    users.to_csv(USER_FILE, index=False)
    return True

# -----------------------------
# 🚪 Auth: Login or Signup
# -----------------------------
st.sidebar.title("🔐 Login / Signup")
auth_mode = st.sidebar.radio("Select Option", ["Login", "Sign Up"])

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if auth_mode == "Login":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    login_btn = st.sidebar.button("Login")

    if login_btn:
        users = load_users()
        user_row = users[(users['username'] == username) & (users['password'] == password)]
        if not user_row.empty:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.business_name = user_row.iloc[0]['business_name']
        else:
            st.sidebar.error("Invalid username or password")

else:
    new_username = st.sidebar.text_input("Create Username")
    new_password = st.sidebar.text_input("Create Password", type="password")
    business_name = st.sidebar.text_input("Your Business Name")
    signup_btn = st.sidebar.button("Sign Up")

    if signup_btn:
        if not new_username or not new_password or not business_name:
            st.sidebar.warning("Please fill in all fields")
        else:
            success = save_user(new_username.strip(), new_password.strip(), business_name.strip())
            if success:
                st.sidebar.success("Account created! You can now log in.")
            else:
                st.sidebar.error("Username already exists.")

# -----------------------------
# ✅ Main App
# -----------------------------
if st.session_state.logged_in:
    st.title(f"📊 LocalBiz Insights - {st.session_state.business_name}")
    st.write("Upload your sales CSV file to begin analysis.")

    uploaded_file = st.file_uploader("Upload your sales data (.csv)", type="csv")

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

            if 'date' in df.columns:
                df['date'] = pd.to_datetime(df['date'], errors='coerce')

            df.dropna(subset=['date', 'product'], inplace=True)
            df.fillna(0, inplace=True)

            if 'sales_amount' in df.columns:
                df['sales_amount'] = pd.to_numeric(df['sales_amount'], errors='coerce').fillna(0)
            if 'units_sold' in df.columns:
                df['units_sold'] = pd.to_numeric(df['units_sold'], errors='coerce').fillna(0)

            st.success("File uploaded and cleaned successfully!")
            st.dataframe(df.head())

            # 📈 Total Sales Over Time
            daily_sales = df.groupby('date')['sales_amount'].sum().reset_index()
            st.subheader("📈 Total Sales Over Time")
            st.line_chart(daily_sales.rename(columns={'date': 'index'}).set_index('index'))

            # 📊 Product Performance
            st.subheader("📊 Product Performance Over Time")
            product_trend = df.groupby(['date', 'product'])['sales_amount'].sum().reset_index()
            product_pivot = product_trend.pivot(index='date', columns='product', values='sales_amount')
            st.line_chart(product_pivot)

            # 🔮 7-Day Forecast
            st.subheader("🔮 7-Day Sales Forecast (Linear Regression)")
            daily_sales['days_since_start'] = (daily_sales['date'] - daily_sales['date'].min()).dt.days
            X = daily_sales[['days_since_start']]
            y = daily_sales['sales_amount']

            model = LinearRegression()
            model.fit(X, y)

            future_days = np.arange(X['days_since_start'].max() + 1, X['days_since_start'].max() + 8).reshape(-1, 1)
            future_preds = model.predict(future_days)
            future_dates = pd.date_range(start=daily_sales['date'].max() + pd.Timedelta(days=1), periods=7)
            forecast_df = pd.DataFrame({'date': future_dates, 'predicted_sales': future_preds})

            full_forecast = pd.concat([
                daily_sales[['date', 'sales_amount']].rename(columns={'sales_amount': 'value'}),
                forecast_df.rename(columns={'predicted_sales': 'value'})
            ])
            st.line_chart(full_forecast.set_index('date'))

        except Exception as e:
            st.error(f"Error processing file: {e}")
else:
    st.warning("👈 Log in or sign up using the sidebar to get started.")
