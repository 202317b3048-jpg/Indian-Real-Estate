import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Madurai Real Estate Analysis",
    layout="wide"
)

# ----------------------------
# Title
# ----------------------------
st.title("🏠 Madurai Real Estate Analytics Dashboard")
st.markdown("Interactive analysis of independent house properties in Madurai")

# ----------------------------
# Load Data
# ----------------------------
@st.cache_data
def load_data():
    return pd.read_excel(
        "Madurai_RealEstate_Data (1).xlsx",
        engine="openpyxl"
    )

df = load_data()

# ----------------------------
# Sidebar Filters
# ----------------------------
st.sidebar.header("🔍 Filter Properties")

localities = st.sidebar.multiselect(
    "Select Locality",
    options=df["Locality"].unique(),
    default=df["Locality"].unique()
)

bhk = st.sidebar.multiselect(
    "Select BHK",
    options=sorted(df["Bedrooms (BHK)"].unique()),
    default=sorted(df["Bedrooms (BHK)"].unique())
)

price_range = st.sidebar.slider(
    "Price Range (INR)",
    int(df["Estimated Sale Price (INR)"].min()),
    int(df["Estimated Sale Price (INR)"].max()),
    (
        int(df["Estimated Sale Price (INR)"].min()),
        int(df["Estimated Sale Price (INR)"].max())
    )
)

# ----------------------------
# Apply Filters
# ----------------------------
filtered_df = df[
    (df["Locality"].isin(localities)) &
    (df["Bedrooms (BHK)"].isin(bhk)) &
    (df["Estimated Sale Price (INR)"].between(price_range[0], price_range[1]))
]

# ----------------------------
# Key Metrics
# ----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Properties",
    len(filtered_df)
)

col2.metric(
    "Avg Price / Sqft (INR)",
    int(filtered_df["Price per Sqft (INR)"].mean())
)

col3.metric(
    "Avg Rental Yield (%)",
    round(filtered_df["Rental Yield (%)"].mean(), 2)
)

col4.metric(
    "Avg Buyer Attraction Score",
    round(filtered_df["Buyer Attraction Score (1-10)"].mean(), 2)
)

# ----------------------------
# Dataset View
# ----------------------------
st.subheader("📋 Property Data")
st.dataframe(filtered_df, use_container_width=True)

# ----------------------------
# Charts
# ----------------------------
st.subheader("📈 Visual Insights")

col1, col2 = st.columns(2)

# Price vs Area
with col1:
    st.markdown("### Built-up Area vs Sale Price")
    fig1, ax1 = plt.subplots()
    ax1.scatter(
        filtered_df["Built-up Area (sqft)"],
        filtered_df["Estimated Sale Price (INR)"]
    )
    ax1.set_xlabel("Built-up Area (sqft)")
    ax1.set_ylabel("Estimated Sale Price (INR)")
    st.pyplot(fig1)

# Locality-wise Average Price
with col2:
    st.markdown("### Average Price by Locality")
    locality_price = (
        filtered_df
        .groupby("Locality")["Estimated Sale Price (INR)"]
        .mean()
        .sort_values()
    )

    fig2, ax2 = plt.subplots()
    locality_price.plot(kind="barh", ax=ax2)
    ax2.set_xlabel("Average Price (INR)")
    ax2.set_ylabel("Locality")
    st.pyplot(fig2)

# ----------------------------
# Buyer Attraction Analysis
# ----------------------------
st.subheader("⭐ Buyer Attraction vs Rental Yield")

fig3, ax3 = plt.subplots()
ax3.scatter(
    filtered_df["Buyer Attraction Score (1-10)"],
    filtered_df["Rental Yield (%)"]
)
ax3.set_xlabel("Buyer Attraction Score")
ax3.set_ylabel("Rental Yield (%)")
st.pyplot(fig3)

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.markdown("✅ **Data Source:** Madurai Real Estate Dataset")

