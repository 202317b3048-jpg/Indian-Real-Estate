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
distance_it_hub = st.number_input("Distance to IT Hub (km)", min_value=0.0, step=0.1)
nearby_schools = st.number_input("Nearby Schools (count)", min_value=0, step=1)
nearby_hospitals = st.number_input("Nearby Hospitals (count)", min_value=0, step=1)

# --------------------------------------------------
# Financial Information
# --------------------------------------------------
st.subheader("💰 Financial Details")

maintenance = st.number_input(
    "Monthly Maintenance (INR)",
    min_value=0,
    step=100
)

rental_yield = st.number_input(
    "Rental Yield (%)",
    min_value=0.0,
    step=0.1
)

buyer_score = st.slider(
    "Buyer Attraction Score (1–10)",
    min_value=1,
    max_value=10
)

# --------------------------------------------------
# Price Estimation Logic
# --------------------------------------------------
if st.button("💰 Estimate Property Value"):

    # Base calculation
    estimated_price = built_up_area * price_per_sqft

    # Adjust price based on property age
    estimated_price *= max(0.7, 1 - (property_age * 0.01))

    # Adjust for furnishing
    if furnishing_status == "Semi-Furnished":
        estimated_price *= 1.05
    elif furnishing_status == "Fully Furnished":
        estimated_price *= 1.10

    # Adjust for parking
    if parking == "Yes":
        estimated_price *= 1.03

    st.success("✅ Property value estimated successfully!")

    # --------------------------------------------------
    # Display Result
    # --------------------------------------------------
    st.subheader("📊 Estimated Property Value")

    st.write(f"**Locality:** {locality}")
    st.write(f"**Property Type:** {property_type}")
    st.write(f"**Built-up Area:** {built_up_area} sqft")
    st.write(f"**Price per Sqft:** ₹{price_per_sqft}")
    st.write(f"**Buyer Attraction Score:** {buyer_score}/10")
    st.write(f"**Rental Yield:** {rental_yield}%")

    st.metric(
        label="💰 Estimated Sale Price (INR)",
        value=f"₹ {estimated_price:,.0f}"
    )

    st.caption("⚠️ Estimated value is indicative and for reference only.")
