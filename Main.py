
         import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Madurai Property Details",
    layout="centered"
)

st.title("🏡 Madurai City Property Details")
st.caption("Enter property information for Madurai")

# Form starts
with st.form("property_form"):
    st.subheader("📍 Basic Property Information")

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

    bedrooms = st.selectbox(
        "Bedrooms (BHK)",
        [1, 2, 3, 4, 5]
    )

    bathrooms = st.selectbox(
        "Bathrooms",
        [1, 2, 3, 4]
    )

    property_age = st.number_input(
        "Property Age (Years)",
        min_value=0,
        step=1
    )

    facing = st.selectbox(
        "Facing",
        ["North", "South", "East", "West", "North-East", "North-West", "South-East", "South-West"]
    )

    furnishing_status = st.selectbox(
        "Furnishing Status",
        ["Unfurnished", "Semi-Furnished", "Fully Furnished"]
    )

    parking = st.radio(
        "Parking Facility",
        ["Yes", "No"]
    )

    st.subheader("📏 Distance & Amenities (Optional)")

    distance_metro = st.number_input(
        "Distance to Metro (km)",
        min_value=0.0,
        step=0.1
    )

    distance_it_hub = st.number_input(
        "Distance to IT Hub (km)",
        min_value=0.0,
        step=0.1
    )

    nearby_schools = st.number_input(
        "Nearby Schools (count)",
        min_value=0,
        step=1
    )

    nearby_hospitals = st.number_input(
        "Nearby Hospitals (count)",
        min_value=0,
        step=1
    )

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

    estimated_price = st.number_input(
        "Estimated Sale Price (INR)",
        min_value=0,
        step=10000
    )

    buyer_score = st.slider(
        "Buyer Attraction Score (1–10)",
        min_value=1,
        max_value=10
    )

    submitted = st.form_submit_button("✅ Submit Property Details")

# Display summary after submission
if submitted:
    st.success("Property details submitted successfully!")

    st.markdown("### 📋 Property Summary")
    st.write({
        "Locality": locality,
        "Property Type": property_type,
        "Built-up Area (sqft)": built_up_area,
        "Price per Sqft (INR)": price_per_sqft,
        "Bedrooms (BHK)": bedrooms,
        "Bathrooms": bathrooms,
        "Property Age (Years)": property_age,
        "Facing": facing,
        "Furnishing Status": furnishing_status,
        "Parking": parking,
        "Distance to Metro (km)": distance_metro,
        "Distance to IT Hub (km)": distance_it_hub,
        "Nearby Schools": nearby_schools,
        "Nearby Hospitals": nearby_hospitals,
        "Monthly Maintenance (INR)": maintenance,
        "Rental Yield (%)": rental_yield,
        "Estimated Sale Price (INR)": estimated_price,
        "Buyer Attraction Score": buyer_score
    })
