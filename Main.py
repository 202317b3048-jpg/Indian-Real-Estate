import streamlit as st
import pandas as pd

# ----------------------------------
# App Title (same style as reference)
# ----------------------------------
st.title("Real Estate Market Analyzer - Madurai")

# ----------------------------------
# Sidebar selection (reference-style)
# ----------------------------------
options = ["Madurai Real Estate Data"]
selected_option = st.sidebar.selectbox(
    "Select a dataset:",
    options
)

# ----------------------------------
# Load dataset function
# ----------------------------------
def load_data():
    return pd.read_excel(
        "Madurai_RealEstate_Data (1).xlsx",
        engine="openpyxl"
    )

df = load_data()

# ----------------------------------
# Show Dataset
# ----------------------------------
st.subheader("Dataset Preview")
st.dataframe(df)

# ----------------------------------
# Summary Statistics
# ----------------------------------
st.subheader("Summary Statistics")
st.write(df.describe())

# ----------------------------------
# Basic Insights (optional but useful)
# ----------------------------------
st.subheader("Key Insights")

st.write("• Average Price per Sqft (INR):", int(df["Price per Sqft (INR)"].mean()))
st.write("• Average Rental Yield (%):", round(df["Rental Yield (%)"].mean(), 2))
st.write("• Average Buyer Attraction Score:", round(df["Buyer Attraction Score (1-10)"].mean(), 2))
