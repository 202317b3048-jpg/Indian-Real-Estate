import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="India Real Estate Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_excel(
        "Real_estate_data_India 2.xlsx",
        sheet_name="Raw data",
        engine="openpyxl"
    )
    return df

df = load_data()

# Title
st.title("🏠 India Real Estate Market Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

states = st.sidebar.multiselect(
    "Select State / UT",
    options=df["State / Union Territory"].unique(),
    default=df["State / Union Territory"].unique()[:5]
)

market_tier = st.sidebar.multiselect(
    "Select Market Tier",
    options=df["Market Tier"].unique(),
    default=df["Market Tier"].unique()
)

filtered_df = df[
    (df["State / Union Territory"].isin(states)) &
    (df["Market Tier"].isin(market_tier))
]

# KPI section
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Price / Sqft (₹)",
    f"{filtered_df['Price/sqft (₹)'].mean():,.0f}"
)

col2.metric(
    "Median House Price 2025 (₹ Lakh)",
    f"{filtered_df['Median House Price (₹ Lakh) -2025'].mean():,.1f}"
)

col3.metric(
    "Avg YoY Price Growth (%)",
    f"{filtered_df['YoY Price Growth (%)'].mean():,.2f}"
)

# Charts
st.subheader("📈 Price Analysis")

col4, col5 = st.columns(2)

# Average price per sqft by state
with col4:
    avg_price_state = (
        filtered_df
        .groupby("State / Union Territory")["Price/sqft (₹)"]
        .mean()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots()
    avg_price_state.plot(kind="bar", ax=ax)
    ax.set_title("Average Price per Sqft by State")
    ax.set_ylabel("₹ per Sqft")
    ax.set_xlabel("State / UT")
    plt.xticks(rotation=45)

    st.pyplot(fig)

# Price growth by tier
with col5:
    growth_tier = (
        filtered_df
        .groupby("Market Tier")["YoY Price Growth (%)"]
        .mean()
    )

    fig, ax = plt.subplots()
    growth_tier.plot(kind="bar", ax=ax, color="green")
    ax.set_title("Average YoY Growth by Market Tier")
    ax.set_ylabel("YoY Growth (%)")
    ax.set_xlabel("Market Tier")
    plt.xticks(rotation=20)

    st.pyplot(fig)

# Data table
st.subheader("📋 Raw Data Preview")
st.dataframe(filtered_df)
