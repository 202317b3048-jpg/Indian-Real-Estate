import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="India Property Price Estimator",
    layout="centered"
)

st.title("🏢 India Property Price Estimator")
st.caption("Estimate property value using India real estate market data")

# --------------------------------------------------
# Upload Excel File
# --------------------------------------------------
st.subheader("📂 Upload Real Estate Dataset")

uploaded_file = st.file_uploader(
    "Upload 'Real_estate_data_India 2.xlsx'",
    type=["xlsx"]
)

if uploaded_file is None:
    st.warning("Please upload the Excel file to continue.")
    st.stop()

# --------------------------------------------------
# Load Data Safely
# --------------------------------------------------
@st.cache_data
def load_data(file):
    return pd.read_excel(
        file,
        sheet_name="Raw data"
    )

try:
    df = load_data(uploaded_file)
except Exception as e:
    st.error(f"❌ Unable to read Excel file: {e}")
    st.stop()

# --------------------------------------------------
# Location Selection
# --------------------------------------------------
st.subheader("📍 Location Details")

state = st.selectbox(
    "State / Union Territory",
    sorted(df["State / Union Territory"].dropna().unique())
)

state_df = df[df["State / Union Territory"] == state]

city = st.selectbox(
    "City",
    sorted(state_df["City"].dropna().unique())
)

row = state_df[state_df["City"] == city].iloc[0]

# Extract values
market_tier = row["Market Tier"]
price_per_sqft = float(row["Price/sqft (₹)"])
median_price = row["Median House Price (₹ Lakh) -2025"]
yoy_growth = float(row["YoY Price Growth (%)"])
cagr_5y = float(row["5-Year CAGR (%)"])

st.info(
    f"""
**Market Tier:** {market_tier}  
**Avg Price / Sqft:** ₹{price_per_sqft:,.0f}  
**Median Price (2025):** ₹{median_price} Lakh
"""
)

# --------------------------------------------------
# Property Inputs
# --------------------------------------------------
st.subheader("🏠 Property Details")

property_type = st.selectbox(
    "Property Type",
    ["Apartment", "Independent House", "Villa", "Plot"]
)

built_up_area = st.number_input(
    "Built-up Area (sqft)",
    min_value=300,
    step=50
)

property_age = st.number_input(
    "Property Age (Years)",
    min_value=0,
    step=1
)

furnishing = st.selectbox(
    "Furnishing Status",
    ["Unfurnished", "Semi-Furnished", "Fully Furnished"]
)

parking = st.radio("Parking Facility", ["Yes", "No"])

# --------------------------------------------------
# Market Metrics
# --------------------------------------------------
st.subheader("📈 Market Indicators")

col1, col2 = st.columns(2)
col1.metric("YoY Growth (%)", f"{yoy_growth}%")
col2.metric("5-Year CAGR (%)", f"{cagr_5y}%")

# --------------------------------------------------
# Estimation Logic
# --------------------------------------------------
if st.button("💰 Estimate Property Value"):

    price = built_up_area * price_per_sqft

    # Age depreciation
    price *= max(0.75, 1 - (property_age * 0.01))

    # Furnishing premium
    if furnishing == "Semi-Furnished":
        price *= 1.05
    elif furnishing == "Fully Furnished":
        price *= 1.10

    # Parking premium
    if parking == "Yes":
        price *= 1.03

    # Market growth
    price *= (1 + yoy_growth / 100)

    st.success("✅ Property value estimated successfully")

    st.metric(
        "💰 Estimated Property Value",
        f"₹ {price:,.0f}"
    )

    st.caption("⚠️ Indicative estimate based on market averages.")
