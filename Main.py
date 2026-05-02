import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Setup
# --------------------------------------------------
st.set_page_config(page_title="Property Price Estimator", layout="centered")

st.title("🏠 Property Price Estimator – India")
st.caption("Select your preferences to estimate property value")

# --------------------------------------------------
# Upload Dataset
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload Real Estate Dataset (Excel)",
    type=["xlsx"]
)

if uploaded_file is None:
    st.info("Please upload the Excel file to continue.")
    st.stop()

# --------------------------------------------------
# Load Data
# --------------------------------------------------
df = pd.read_excel(uploaded_file, sheet_name="Raw data")

# --------------------------------------------------
# User Preferences
# --------------------------------------------------
st.subheader("📍 Location Preference")

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

# --------------------------------------------------
# Property Details
# --------------------------------------------------
st.subheader("🏢 Property Details")

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

# --------------------------------------------------
# Estimation
# --------------------------------------------------
if st.button("💰 Estimate Property Price"):

    # Base calculation
    estimated_price = area * price_per_sqft

    # Age depreciation
    estimated_price *= max(0.75, 1 - property_age * 0.01)

    # Furnishing premium
    if furnishing == "Semi-Furnished":
        estimated_price *= 1.05
    elif furnishing == "Fully Furnished":
        estimated_price *= 1.10

    # Market growth
    estimated_price *= (1 + yoy_growth / 100)

    # --------------------------------------------------
    # Result
    # --------------------------------------------------
    st.success("✅ Estimation Complete!")

    st.subheader("📊 Estimated Property Value")

    st.write(f"**State:** {state}")
    st.write(f"**City:** {city}")
    st.write(f"**Area:** {area} sqft")
    st.write(f"**Price per Sqft:** ₹{price_per_sqft:,.0f}")

    st.metric(
        "💰 Estimated Price (INR)",
        f"₹ {estimated_price:,.0f}"
    )

    st.caption("⚠️ This is a market-based indicative estimate.")
