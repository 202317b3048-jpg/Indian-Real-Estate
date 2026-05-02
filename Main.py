import streamlit as st
import pandas as pd

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Indian Real Estate Estimator",
    layout="centered"
)

st.title("🏠 Indian Real Estate Price Estimator")
st.caption("Select your preferences to estimate property value")

# -------------------------------
# Upload Dataset
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload Indian Real Estate Dataset (Excel)",
    type=["xlsx"]
)

if uploaded_file is None:
    st.info("Please upload the Excel file to continue.")
    st.stop()

# -------------------------------
# Load Data
# -------------------------------
df = pd.read_excel(uploaded_file, sheet_name="Raw data")

# -------------------------------
# Location Selection
# -------------------------------
st.subheader("📍 Location Preferences")

state = st.selectbox(
    "Select State / Union Territory",
    sorted(df["State / Union Territory"].dropna().unique())
)

state_df = df[df["State / Union Territory"] == state]

city = st.selectbox(
    "Select City",
    sorted(state_df["City"].dropna().unique())
)

city_data = state_df[state_df["City"] == city].iloc[0]

price_per_sqft = city_data["Price/sqft (₹)"]
yoy_growth = city_data["YoY Price Growth (%)"]

# -------------------------------
# Property Preferences
# -------------------------------
st.subheader("🏢 Property Preferences")

area = st.number_input(
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

parking = st.radio(
    "Parking Available",
    ["Yes", "No"]
)

# -------------------------------
# Estimation Logic
# -------------------------------
if st.button("💰 Estimate Property Value"):

    estimated_price = area * price_per_sqft

    # Depreciation based on age
    estimated_price *= max(0.75, 1 - property_age * 0.01)

    # Furnishing premium
    if furnishing == "Semi-Furnished":
        estimated_price *= 1.05
    elif furnishing == "Fully Furnished":
        estimated_price *= 1.10

    # Parking premium
    if parking == "Yes":
        estimated_price *= 1.03

    # Market growth adjustment
    estimated_price *= (1 + yoy_growth / 100)

    # -------------------------------
    # Display Result
    # -------------------------------
    st.success("✅ Property Value Estimated")

    st.subheader("📊 Estimated Property Value")

    st.write(f"**State:** {state}")
    st.write(f"**City:** {city}")
