import streamlit as st

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Madurai Property Price Estimator",
    layout="centered"
)

st.title("🏡 Madurai Property Price Estimator")
st.caption("Select your preferences to get an estimated property value")

# ---------------------------
# User Inputs
# ---------------------------
st.subheader("📋 Property Preferences")

locality = st.selectbox(
    "Select Locality",
    ["Anna Nagar", "KK Nagar", "Mattuthavani", "SS Colony", "Tallakulam", "Villapuram"]
)

property_type = st.selectbox(
    "Property Type",
    ["Apartment", "Independent House", "Villa"]
)

built_up_area = st.number_input(
    "Built-up Area (sqft)",
    min_value=300,
    step=50
)

bedrooms = st.selectbox(
    "Bedrooms (BHK)",
    [1, 2, 3, 4]
)

# ---------------------------
# Base price per sqft (sample values)
# ---------------------------
price_dict = {
    "Anna Nagar": 5500,
    "KK Nagar": 5000,
    "Mattuthavani": 4200,
    "SS Colony": 4500,
    "Tallakulam": 6000,
    "Villapuram": 3800
}

type_multiplier = {
    "Apartment": 1.0,
    "Independent House": 1.2,
    "Villa": 1.4
}

# ---------------------------
# Estimate Button
# ---------------------------
if st.button("💰 Estimate Property Price"):
    base_price = price_dict[locality]
    multiplier = type_multiplier[property_type]

    estimated_price = built_up_area * base_price * multiplier

    st.success("✅ Property Value Estimated!")

    st.subheader("📊 Estimated Result")
    st.write(f"**Locality:** {locality}")
    st.write(f"**Property Type:** {property_type}")
    st.write(f"**Area:** {built_up_area} sqft")
    st.write(f"**Bedrooms:** {bedrooms} BHK")

    st.metric(
        "Estimated Property Value",
        f"₹ {estimated_price:,.0f}"
    )

    st.caption("⚠️ This is an approximate value for reference only.")
