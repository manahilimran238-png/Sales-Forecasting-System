# 📈 Sales Forecasting System

A data science and machine learning project that analyzes historical sales data and predicts future sales using time-based features and Random Forest Regression.

## 🎯 Project Objective

Businesses need accurate sales forecasts to support inventory management, revenue planning, and business decision-making.

This project analyzes historical sales patterns and builds a machine learning model to forecast future sales based on historical information.

## 📂 Dataset

The project uses a retail sales dataset containing historical sales information for multiple stores and product families.

The dataset includes information such as:

- Date
- Store
- Product family
- Sales
- Transactions
- Store information
- Holidays and events
- Oil prices

The training dataset contains approximately **3 million records** covering the period from **2013 to 2017**.

## 🔄 Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Data Aggregation
5. Feature Engineering
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Future Sales Forecasting

## 📊 Exploratory Data Analysis

The project analyzes:

- Sales trends over time
- Yearly and monthly sales patterns
- Daily sales patterns
- Store-level sales
- Product-family sales
- Seasonal behavior

Visualizations were created using Matplotlib to understand historical sales patterns.

## ⚙️ Feature Engineering

Several time-based and historical sales features were created:

- Year
- Month
- Day
- Day of Week
- Week of Year
- Lag 1
- Lag 7
- Lag 30

Lag features allow the model to use previous sales information when making predictions.

## 🤖 Machine Learning Model

A **Random Forest Regressor** was used to predict sales.

The data was divided chronologically into training and testing sets to avoid using future information when training the model.

### Training Period

2013-01-31 to 2016-09-17

### Testing Period

2016-09-18 to 2017-08-15

## 📏 Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

### Results

| Metric | Result |
|---|---:|
| MAE | 85,072.90 |
| RMSE | 134,979.14 |
| Average Actual Sales | 850,957.98 |
| MAE as % of Average Sales | 10.00% |

The model achieved an MAE equivalent to approximately **10% of the average daily sales**, providing a useful baseline for sales forecasting.

## 🔮 Future Sales Forecast

The trained model was used to generate a **30-day future sales forecast**.

| Forecast Metric | Value |
|---|---:|
| Average Predicted Daily Sales | 823,747.05 |
| Highest Predicted Daily Sales | 1,173,482.16 |
| Lowest Predicted Daily Sales | 649,985.15 |
| Total Predicted Sales | 24,712,411.46 |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab
- Jupyter Notebook

## 📁 Project Structure

```text
Sales-Forecasting-System/
│
├── Sales_Forecasting_System.ipynb
└── README.md
