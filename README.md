# 📊 LocalBiz Insights

**LocalBiz Insights** is a lightweight, interactive data analytics dashboard built with Streamlit. It helps small businesses quickly visualize sales trends, monitor product performance, and forecast future sales — all by simply uploading a CSV file.

---

## 🚀 Features

- 📈 Upload and analyze sales data from CSV
- 🧹 Automatic data cleaning & validation
- 🛍️ Product-wise sales performance trends
- 🔮 7-day sales forecasting (Linear Regression)
- 🧾 Login & Sign-up system (user authentication)
- 📦 Lightweight, easy to deploy

---

## 📸 Preview
![Screenshot 2025-07-09 124301](https://github.com/user-attachments/assets/d6f324f6-2854-48b2-a0ae-1d0795937996)
![Screenshot 2025-07-09 124336](https://github.com/user-attachments/assets/bc95bf20-70bc-4a75-91dc-d2ba8603104c)



---

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [NumPy](https://numpy.org/)

---

## 📂 Project Structure

LocalBiz-Insights/
├── app.py # Main Streamlit app
├── users.csv # Stores registered users
├── sample_data/ # Example sales CSVs
│ └── sales_data.csv
├── requirements.txt # Python dependencies
└── README.md # Project documentation



---

## 📈 Sample Data Format

Ensure your uploaded CSV includes the following columns:

| date       | product      | sales_amount | units_sold |
|------------|--------------|---------------|------------|
| 2024-01-01 | Chocolate Bar| 200.0         | 20         |
| 2024-01-02 | Cookie       | 150.0         | 15         |

---

## 🌐 Live Demo

> [https://localbiz-insights-aarya1.streamlit.app/]

---

## 🚀 Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/aarya-patel1/LocalBiz-Insights.git
cd LocalBiz-Insights
```
🛡️ Login Info (for testing)
Use the signup form in the app to create your own account, or edit users.csv to preload users.

🧠 Future Ideas
🔐 Hashed passwords with bcrypt

🧾 Per-user saved CSVs

🌍 Multi-language support

🧠 Advanced forecasting (Prophet, ARIMA)

📬 Contact
Made with ❤️ by Aarya Patel
