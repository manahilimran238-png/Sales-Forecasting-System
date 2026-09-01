# 📈 Sales Forecasting System

A data science and machine learning project that analyzes historical retail sales data and predicts future sales using time-based features and a **Random Forest Regressor**.

The project also includes an interactive **Streamlit web application** for generating and visualizing future sales forecasts.

## 🎯 Project Objective

Businesses need reliable sales forecasts to support inventory management, revenue planning, and business decision-making.

This project analyzes historical sales patterns, aggregates sales data on a daily basis, and builds a machine learning model to forecast future sales based on time-based features.

## 📂 Dataset

The project uses a retail sales dataset containing historical sales information for multiple stores and product families.

The dataset includes information such as:

* Date
* Store
* Product Family
* Sales
* Transactions
* Store Information
* Holidays and Events
* Oil Prices

The training dataset contains approximately **3 million records** covering the period from **2013 to 2017**.

## 🔄 Project Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Daily Sales Aggregation
5. Feature Engineering
6. Chronological Train-Test Split
7. Model Training
8. Model Evaluation
9. Future Sales Forecasting
10. Streamlit Web Application

## 📊 Exploratory Data Analysis

The project analyzes historical sales patterns through visualizations including:

* Daily sales trends
* Monthly sales patterns
* Seasonal sales behavior
* Yearly sales patterns
* Historical sales fluctuations

Visualizations were created using **Matplotlib** and **Seaborn** to better understand the behavior of sales over time.

## ⚙️ Feature Engineering

The forecasting model uses the following time-based features:

* **Year**
* **Month**
* **Day**
* **Day of Week**
* **Week of Year**

These features allow the model to identify patterns related to different dates, months, weekdays, and weeks of the year.

## 🤖 Machine Learning Model

A **Random Forest Regressor** was used to predict daily sales.

Model configuration:

* `n_estimators = 100`
* `random_state = 42`
* `n_jobs = -1`

The data was divided chronologically into training and testing sets to preserve the time-based nature of the forecasting problem.

### Training Period

**2013-01-31 to 2016-09-17**

### Testing Period

**2016-09-18 to 2017-08-15**

## 📏 Model Evaluation

The model was evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)

### Results

| Metric                    |     Result |
| ------------------------- | ---------: |
| MAE                       |  85,072.90 |
| RMSE                      | 134,979.14 |
| Average Actual Sales      | 850,957.98 |
| MAE as % of Average Sales |     10.00% |

The model achieved an MAE equivalent to approximately **10% of the average daily sales**, providing a useful baseline for sales forecasting.

## 🔮 Future Sales Forecast

After evaluation, a final Random Forest model was trained using all available historical data.

The model was then used to generate a **30-day future sales forecast**.

### 30-Day Forecast Results

| Forecast Metric               |         Value |
| ----------------------------- | ------------: |
| Average Predicted Daily Sales |    823,747.05 |
| Highest Predicted Daily Sales |  1,173,482.16 |
| Lowest Predicted Daily Sales  |    649,985.15 |
| Total Predicted Sales         | 24,712,411.46 |

## 🌐 Streamlit Web Application

The project includes an interactive Streamlit application that allows users to generate future sales forecasts without running the complete Jupyter Notebook.

### Application Features

* 📊 Historical sales visualization
* 🔮 7-day, 14-day, and 30-day forecasting
* 📈 Future sales forecast visualization
* 📌 Forecast summary metrics
* 📋 Detailed forecast table
* ⬇️ Downloadable forecast CSV file

## 🚀 Live Demo

The live Streamlit application will be available here:

**[Sales Forecasting System – Live App](YOUR_STREAMLIT_APP_URL)**

> Replace `YOUR_STREAMLIT_APP_URL` with the Streamlit URL after deployment.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Google Colab
* Jupyter Notebook

## 📁 Project Structure

```text
Sales-Forecasting-System/
│
├── Sales_Forecasting_System.ipynb
├── README.md
├── train.csv.zip
├── app.py
├── daily_sales.csv
├── sales_forecasting_model.pkl
└── requirements.txt
```

## ▶️ Run the Streamlit App Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Sales-Forecasting-System
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📌 Key Outcome

This project demonstrates an end-to-end machine learning workflow for sales forecasting, including:

**Data Analysis → Feature Engineering → Model Training → Evaluation → Future Forecasting → Interactive Deployment**

The Streamlit application makes the trained forecasting model accessible through a simple and user-friendly interface.

