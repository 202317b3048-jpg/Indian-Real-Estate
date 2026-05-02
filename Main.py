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
st.caption("Estimate property value using real estate market data across India")

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_excel(
        "Real_estate_data_India 2.xlsx",
        sheet_name="Raw data",
        engine="openpyxl"
    )

df = load_data()

# --------------------------------------------------
# Property Location Selection
# --------------------------------------------------
st.subheader("📍 Location Details")

state = st.selectbox(
    "State / Union Territory",
    sorted(df["State / Union Territory"].unique())
)

city_df = df[df["State / Union Territory"] == state]

city = st.selectbox(
    "City",
    sorted(city_df["City"].dropna().unique())
)

row = city_df[city_df["City"] == city].iloc[0]

market_tier = row["Market Tier"]
avg_price_per_sqft = row["Price/sqft (₹)"]
median_price_2025 = row["Median House Price (₹ Lakh) -2025"]

st.info(f"""
**Market Tier:** {market_tier}  
**Avg Price / Sqft:** ₹{avg_price_per_sqft:,.0f}  
**Median House Price (2025):** ₹{median_price_2025} Lakh
""")

# --------------------------------------------------
# Property Details
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

bedrooms = st.selectbox("Bedrooms (BHK)", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])

property_age = st.number_input(
    "Property Age (Years)",
    min_value=0,
    step=1
)

furnishing_status = st.selectbox(
    "Furnishing Status",
    ["Unfurnished", "Semi-Furnished", "Fully Furnished"]
)

parking = st.radio("Parking Facility", ["Yes", "No"])

# --------------------------------------------------
# Investment Metrics (Dataset Based)
# --------------------------------------------------
st.subheader("📈 Market Indicators")

yoy_growth = row["YoY Price Growth (%)"]
cagr_5y = row["5-Year CAGR (%)"]

st.metric("YoY Price Growth (%)", f"{yoy_growth}%")
st.metric("5-Year CAGR (%)", f"{cagr_5y}%")

# --------------------------------------------------
# Price Estimation Logic
# --------------------------------------------------
if st.button("💰 Estimate Property Value"):

    # Base Price
    estimated_price = built_up_area * avg_price_per_sqft

    # Property age depreciation
    estimated_price *= max(0.75, 1 - (property_age * 0.01))

    # Furnishing premium
    if furnishing_status == "Semi-Furnished":
        estimated_price *= 1.05
    elif furnishing_status == "Fully Furnished":
        estimated_price *= 1.10

    # Parking premium
    if parking == "Yes":
        estimated_price *= 1.03

    # Market growth bonus
    estimated_price *= (1 + yoy_growth / 100)

    st.success("✅ Property value estimated successfully!")

    # --------------------------------------------------
    # Display Result
    # --------------------------------------------------
    st.subheader("📊 Estimated Property Value")

    st.write(f"**State:** {state}")
    st.write(f"**City:** {city}")
    st.write(f"**Property Type:** {property_type}")
    st.write(f"**Built-up Area:** {built_up_area} sqft")
    st.write(f"**Market Tier:** {market_tier}")

    st.metric(
        label="💰 Estimated Sale Price (INR)",
        value=f"₹ {estimated_price:,.0f}"
    )

    st.caption("⚠️ This estimate is derived from market averages and should be used for reference only.")
