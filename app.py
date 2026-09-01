import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Sales Forecasting System",
    page_icon="📈",
    layout="wide"
)


# -----------------------------
# Load Model
# -----------------------------

@st.cache_resource
def load_model():
    return joblib.load("sales_forecasting_model.pkl")


# -----------------------------
# Load Historical Data
# -----------------------------

@st.cache_data
def load_data():
    data = pd.read_csv("daily_sales.csv")
    data["date"] = pd.to_datetime(data["date"])
    return data


model = load_model()
historical_data = load_data()


# -----------------------------
# Title
# -----------------------------

st.title("📈 Sales Forecasting System")

st.write(
    "A machine learning system that forecasts future daily sales "
    "using a Random Forest Regressor."
)


# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.header("Forecast Settings")

forecast_days = st.sidebar.selectbox(
    "Select Forecast Period",
    [7, 14, 30],
    index=2
)


# -----------------------------
# Historical Sales
# -----------------------------

st.subheader("📊 Historical Sales")

recent_history = historical_data.tail(60)

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    recent_history["date"],
    recent_history["sales"],
    label="Historical Sales"
)

ax.set_title("Recent Historical Sales")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
ax.grid(True, alpha=0.3)
ax.legend()

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)


# -----------------------------
# Generate Forecast
# -----------------------------

if st.button("🔮 Generate Forecast", use_container_width=True):

    last_date = historical_data["date"].max()

    future_dates = pd.date_range(
        start=last_date + pd.Timedelta(days=1),
        periods=forecast_days,
        freq="D"
    )

    future_data = pd.DataFrame({
        "date": future_dates
    })

    # Create the same features used during model training

    future_data["year"] = future_data["date"].dt.year
    future_data["month"] = future_data["date"].dt.month
    future_data["day"] = future_data["date"].dt.day
    future_data["day_of_week"] = future_data["date"].dt.dayofweek
    future_data["week_of_year"] = (
        future_data["date"].dt.isocalendar().week.astype(int)
    )

    # Select model features

    features = [
        "year",
        "month",
        "day",
        "day_of_week",
        "week_of_year"
    ]

    X_future = future_data[features]

    # Generate predictions

    predictions = model.predict(X_future)

    future_data["Predicted Sales"] = predictions

    # -----------------------------
    # Forecast Summary
    # -----------------------------

    st.subheader("📌 Forecast Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Average Daily Sales",
            f"{predictions.mean():,.0f}"
        )

    with col2:
        st.metric(
            "Highest Predicted Sales",
            f"{predictions.max():,.0f}"
        )

    with col3:
        st.metric(
            "Lowest Predicted Sales",
            f"{predictions.min():,.0f}"
        )

    with col4:
        st.metric(
            f"Total ({forecast_days} Days)",
            f"{predictions.sum():,.0f}"
        )

    # -----------------------------
    # Forecast Graph
    # -----------------------------

    st.subheader("📈 Sales Forecast")

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        recent_history["date"],
        recent_history["sales"],
        label="Historical Sales"
    )

    ax.plot(
        future_data["date"],
        future_data["Predicted Sales"],
        label="Future Forecast",
        linestyle="--"
    )

    ax.axvline(
        x=last_date,
        linestyle=":"
    )

    ax.set_title(
        f"{forecast_days}-Day Sales Forecast"
    )

    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")

    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()

    st.pyplot(fig)

    # -----------------------------
    # Forecast Table
    # -----------------------------

    st.subheader("📋 Forecast Details")

    display_data = future_data.copy()

    display_data["date"] = display_data["date"].dt.date

    display_data["Predicted Sales"] = display_data[
        "Predicted Sales"
    ].round(2)

    st.dataframe(
        display_data,
        use_container_width=True
    )

    # -----------------------------
    # Download Forecast
    # -----------------------------

    csv = future_data.to_csv(index=False)

    st.download_button(
        label="⬇️ Download Forecast CSV",
        data=csv,
        file_name="sales_forecast.csv",
        mime="text/csv"
    )
