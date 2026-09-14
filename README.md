# 📈 Sales Forecasting System

A sales forecasting system that analyzes historical retail sales data, identifies time-based patterns, and predicts future sales using a Random Forest Regressor — with an interactive Streamlit dashboard for generating and visualizing forecasts.

🔗 **Live demo:** (https://sales-forecasting-system-bpecypj3gmrkmjphvrjqvk.streamlit.app/)

---

## 📌 Overview

Businesses need reliable sales forecasts to support inventory planning, revenue estimation, and data-driven decision-making. This project analyzes historical retail sales, aggregates sales on a daily basis, extracts time-based features, and builds a forecasting model to estimate future sales.

The project also includes an interactive Streamlit application where users can explore historical sales and generate forecasts for different time horizons.

## ✨ Features

* **Exploratory Data Analysis** — analyzes daily, monthly, yearly, and seasonal sales patterns
* **Data Preparation** — cleans and prepares historical retail sales data for forecasting
* **Daily Sales Aggregation** — converts transaction-level sales into daily sales totals
* **Time-Based Feature Engineering** — extracts year, month, day, day of week, and week of year
* **Random Forest Forecasting** — trains a Random Forest Regressor to predict daily sales
* **Chronological Train-Test Split** — preserves the time-based structure of the forecasting problem
* **Model Evaluation** — evaluates predictions using MAE and RMSE
* **Future Forecasting** — generates 7-day, 14-day, and 30-day sales forecasts
* **Forecast Visualization** — displays historical and predicted sales trends
* **Forecast Summary** — provides average, highest, lowest, and total predicted sales
* **CSV Export** — allows forecast results to be downloaded for further analysis
* **Interactive Streamlit App** — provides a simple interface for exploring data and generating forecasts

## 🖼️ Screenshots

<img width="1278" height="563" alt="image" src="https://github.com/user-attachments/assets/a006a27f-1ef0-4505-b2e8-02250a17da27" />


## 🗂️ Project Structure

```text
Sales-Forecasting-System/
├── Sales_Forecasting_System.ipynb
├── app.py
├── daily_sales.csv
├── sales_forecasting_model.pkl
├── train.csv.zip
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* pip

### Installation

```bash
# Clone the repository
git clone https://github.com/manahilimran238-png/Sales-Forecasting-System.git
cd Sales-Forecasting-System

# Install dependencies
pip install -r requirements.txt
```

### Usage

Launch the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

To explore the complete analysis and model development:

```text
Sales_Forecasting_System.ipynb
```

## 📊 Dataset

The project uses historical retail sales data containing information from multiple stores and product families.

The dataset contains approximately **3 million records** covering **2013–2017**.

| Feature           | Description                          |
| ----------------- | ------------------------------------ |
| `Date`            | Sales date                           |
| `Store`           | Store identifier                     |
| `Product Family`  | Product category/family              |
| `Sales`           | Daily sales value                    |
| `Transactions`    | Number of transactions               |
| Store Information | Additional store-related information |
| Holidays & Events | Holiday and event information        |
| Oil Prices        | Historical oil price information     |

For forecasting, transaction-level sales are aggregated into daily sales totals and time-based features are extracted from the date.

## 🧠 Model Performance

A **Random Forest Regressor** was used for daily sales forecasting.

### Model Configuration

| Parameter      | Value |
| -------------- | ----: |
| `n_estimators` |   100 |
| `random_state` |    42 |
| `n_jobs`       |    -1 |

A chronological train-test split was used to preserve the temporal structure of the data.

| Metric                     |     Result |
| -------------------------- | ---------: |
| MAE                        |  85,072.90 |
| RMSE                       | 134,979.14 |
| Average Actual Daily Sales | 850,957.98 |
| MAE as % of Average Sales  |     10.00% |

The model achieved an MAE equivalent to approximately **10% of average daily sales** on the test period.

### Key insight

The forecasting model captures useful time-based sales patterns from historical data, providing a practical baseline for estimating future daily sales.

## 🔮 Future Forecast

The final Random Forest model was used to generate a **30-day future sales forecast**.

| Forecast Metric               |         Value |
| ----------------------------- | ------------: |
| Average Predicted Daily Sales |    823,747.05 |
| Highest Predicted Daily Sales |  1,173,482.16 |
| Lowest Predicted Daily Sales  |    649,985.15 |
| Total Predicted Sales         | 24,712,411.46 |

The Streamlit application also supports **7-day, 14-day, and 30-day** forecast horizons.

## 🛠️ Tech Stack

`Python` · `Pandas` · `NumPy` · `Scikit-learn` · `Matplotlib` · `Seaborn` · `Streamlit` · `Joblib` · `Jupyter Notebook`

## 🗺️ Roadmap / Possible Extensions

* [ ] Add lag and rolling-window features for improved temporal forecasting
* [ ] Compare Random Forest with dedicated time-series models
* [ ] Add store- and product-level forecasting
* [ ] Add interactive date-range and store filters to the dashboard
* [ ] Add automated forecast accuracy monitoring
* [ ] Deploy the Streamlit application publicly

## 📄 License

This project is licensed under the MIT License.



