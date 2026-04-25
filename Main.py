import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Madurai Property Price Estimator",
    layout="centered"
)

st.title("🏡 Madurai Property Price Estimator")
st.caption("Select your preferences to estimate the property value in Madurai")

# --------------------------------------------------
# Property Details Input
# --------------------------------------------------
st.subheader("📋 Property Details")

locality = st.text_input("Locality")

property_type = st.selectbox(
    "Property Type",
    ["Apartment", "Independent House", "Villa", "Plot"]
)

built_up_area = st.number_input(
    "Built-up Area (sqft)",
    min_value=100,
    step=10
)

price_per_sqft = st.number_input(
    "Price per Sqft (INR)",
    min_value=500,
    step=100
)

bedrooms = st.selectbox("Bedrooms (BHK)", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])

property_age = st.number_input(
    "Property Age (Years)",
    min_value=0,
    step=1
)

facing = st.selectbox(
    "Facing",
    ["North", "South", "East", "West",
     "North-East", "North-West", "South-East", "South-West"]
)

furnishing_status = st.selectbox(
    "Furnishing Status",
    ["Unfurnished", "Semi-Furnished", "Fully Furnished"]
)

parking = st.radio("Parking Facility", ["Yes", "No"])

# --------------------------------------------------
# Optional Distance & Amenities
# --------------------------------------------------
st.subheader("📏 Distance & Amenities (Optional)")

distance_metro = st.number_input("Distance to Metro (km)", min_value=0.0, step=0.1)

   
