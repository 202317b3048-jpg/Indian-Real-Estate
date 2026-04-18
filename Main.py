import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="Madurai Real Estate Dashboard",
    layout="wide"
)

# Title
st.title("🏡 Madurai Real Estate Dashboard")
st.caption("Based on local property data from Madurai")

# Load Excel data
@st.cache_data
def load_data():
    df = pd.read_excel(
        "Madurai_RealEstate_Data (1).xlsx",
        engine="openpyxl"
    )
    return df

df = load_data()

# Show raw data
st.subheader("📊 Raw Property Data")
st.dataframe(df)

# Sidebar filters
st.sidebar.header("🔍 Filters")

locality = st.sidebar.selectbox(
    "Select Locality",
    options=["All"] + sorted(df["Locality"].unique().tolist())
)

bhk = st.sidebar.selectbox(
    "Select BHK",
    options=["All"] + sorted(df["Bedrooms (BHK)"].unique().tolist())
)

# Apply filters
filtered_df = df.copy()

if locality != "All":
    filtered_df = filtered_df[filtered_df["Locality"] == locality]

if bhk != "All":
    filtered_df = filtered_df[filtered_df["Bedrooms (BHK)"] == bhk]

# Filtered data view
st.subheader("🏘️ Filtered Properties")
st.dataframe(filtered_df)

# KPIs
st.subheader("📈 Key Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Price / Sqft (₹)",
        f"{int(filtered_df['Price per Sqft (INR)'].mean())}"
    )

with col2:
    st.metric(
        "Average Sale Price (₹)",
        f"{int(filtered_df['Estimated Sale Price (INR)'].mean())}"
    )

with col3:
    st.metric(
        "Avg Buyer Attraction Score",
        round(filtered_df["Buyer Attraction Score (1-10)"].mean(), 2)
    )

# Chart: Price per sqft by locality
st.subheader("📊 Average Price per Sqft by Locality")

price_chart = (
    filtered_df
    .groupby("Locality")["Price per Sqft (INR)"]
    .mean()
)

st.bar_chart(price_chart)

# Footer
st.markdown("---")
st.caption("📍 Madurai | Real Estate Analysis using Streamlit & Excel")
