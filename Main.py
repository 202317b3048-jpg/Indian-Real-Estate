import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Madurai Property Details",
    layout="centered"
)

st.title("🏡 Madurai City Property Details")
st.caption("Enter property information for Madurai")

# Initialize session state
if "submitted_data" not in st.session_state:
    st.session_state.submitted_data = []

# =========================
# Property Form
# =========================
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

    st.subheader("📏 Distance & Amenities (Optional)")

    distance_metro = st.number_input(
        "Distance to Metro (km)",
        min_value=0.0,
        step=0.1,
        help="Enter 0 if metro is not nearby"
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

    buyer_score = st.slider(
        "Buyer Attraction Score (1–10)",
        min_value=1,
        max_value=10
    )

    submitted = st.form_submit_button("✅ Submit Property Details")

# =========================
# After Submission
# =========================
if submitted:
    st.success("Property details submitted successfully!")

    # Calculations
    calculated_price = built_up_area * price_per_sqft

    if calculated_price < 40_00_000:
        price_segment = "Budget"
    elif calculated_price < 80_00_000:
        price_segment = "Mid-range"
    else:
        price_segment = "Premium"

    if buyer_score >= 8:
        buyer_insight = "🔥 High Buyer Demand"
    elif buyer_score >= 5:
        buyer_insight = "✅ Moderate Buyer Demand"
    else:
        buyer_insight = "⚠️ Low Buyer Demand"

    # Warnings
    if rental_yield > 15:
        st.warning("Rental Yield seems unusually high.")

    if property_age > 25:
        st.warning("Older property – resale value may be impacted.")

    # Data dictionary
    property_data = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Locality": locality,
        "Property Type": property_type,
        "Built-up Area (sqft)": built_up_area,
        "Price per Sqft": price_per_sqft,
        "Calculated Price": calculated_price,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Property Age": property_age,
        "Facing": facing,
        "Furnishing": furnishing_status,
        "Parking": parking,
        "Metro Distance (km)": distance_metro,
        "IT Hub Distance (km)": distance_it_hub,
        "Schools Nearby": nearby_schools,
        "Hospitals Nearby": nearby_hospitals,
        "Maintenance": maintenance,
        "Rental Yield (%)": rental_yield,
        "Buyer Score": buyer_score,
        "Buyer Insight": buyer_insight,
        "Price Segment": price_segment
    }

    # Save to CSV
    df = pd.DataFrame([property_data])
    df.to_csv(
        "madurai_property_data.csv",
        mode="a",
        header=not st.session_state.submitted_data,
        index=False
    )

    st.session_state.submitted_data.append(property_data)

    # =========================
    # Display Summary
    # =========================
    st.markdown("### 📋 Property Summary")
    st.json(property_data)

    # Insights
    st.markdown("### 📊 Market Insights")
    st.write(f"**Calculated Property Price:** ₹{calculated_price:,.0f}")
    st.write(f"**Price Category:** {price_segment}")
    st.write(f"**Buyer Demand:** {buyer_insight}")
      
