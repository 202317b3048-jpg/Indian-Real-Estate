import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Madurai Real Estate Market Dashboard", layout="wide")
st.title("🏠 Madurai Real Estate Market Dashboard")

# Debug: show current files (helps detect name issues)
st.write("Files in current directory:", os.listdir("."))

@st.cache_data
def load_data():
    return pd.read_excel("Madurai_RealEstate_Data (1).xlsx")

df = load_data()

st.subheader("📄 Dataset Preview")
st.dataframe(df)

st.subheader("📊 Summary Statistics")
st.write(df.describe())

st.subheader("💰 Average Price per Sqft by Locality")
st.bar_chart(df.groupby("Locality")["Price per Sqft (INR)"].mean())

st.subheader("📐 Built-up Area vs Sale Price")
st.scatter_chart(df[["Built-up Area (sqft)", "Estimated Sale Price (INR)"]])

st.subheader("🪑 Furnishing Status Distribution")
st.bar_chart(df["Furnishing Status"].value_counts())
