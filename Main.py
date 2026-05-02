import streamlit as st

# -----------------------------
# App Title
# -----------------------------
st.set_page_config(page_title="Indian Real Estate Price Estimator", layout="centered")
st.title("🏠 Indian Real Estate Price Estimator")

st.write("Select your preferences to estimate the property value.")

# -----------------------------
# City-wise base price per sq.ft (₹)
# -----------------------------
city_price = {
    "Bangalore": 7500,
    "Chennai": 6500,
    "Hyderabad": 6000,
    "Mumbai": 12000,
    "Delhi": 9000,
    "Pune": 7000,
    "Coimbatore": 5000,
    "Madurai": 4200
}

# -----------------------------
# User Inputs
# -----------------------------
city = st.selectbox("📍 Select City", list(city_price.keys()))

property_type = st.radio(
    "🏢 Property Type",
    ["Apartment", "Independent House"]
)

area_sqft = st.slider(
    "📐 Built-up Area (in sq.ft)",
    min_value=500,
    max_value=5000,
    step=50,
    value=1000
)

bhk = st.selectbox(
    "🛏️ Number of Bedrooms (BHK)",
    [1, 2, 3, 4, 5]
)

property_age = st.slider(
    "🏗️ Property Age (Years)",
    min_value=0,
    max_value=30,
    value=5
)

amenities = st.multiselect(
    "⭐ Amenities",
    ["Parking", "Lift", "Power Backup", "Gym", "Swimming Pool", "Security"]
)

# -----------------------------
# Price Calculation Logic
# -----------------------------
base_price = city_price[city] * area_sqft

# Property type adjustment
if property_type == "Independent House":
    base_price *= 1.15

# BHK factor
bhk_factor = 1 + (bhk - 1) * 0.10
base_price *= bhk_factor

# Depreciation based on property age
age_depreciation = max(0.6, 1 - (property_age * 0.01))
base_price *= age_depreciation

# Amenities premium
amenities_bonus = 1 + (len(amenities) * 0.03)
final_price = base_price * amenities_bonus

# -----------------------------
# Display Result
# -----------------------------
st.markdown("---")
if st.button("💰 Estimate Property Price"):
    st.subheader("📊 Estimated Property Value")
    st.success(f"₹ {final_price:,.0f}")

    st.caption("⚠️ This is an approximate estimate based on selected preferences.")
