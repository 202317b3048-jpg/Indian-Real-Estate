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

