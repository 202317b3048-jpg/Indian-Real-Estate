import streamlit as st
import pandas as pd

st.set_page_config(page_title="Madurai Real Estate Market Dashboard", layout="wide")
st.title("🏠 Madurai Real Estate Market Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("Madurai_RealEstate_Data.csv")

df = load_data()

st.subheader("📄 Dataset Preview")
st.dataframe(df)

st.subheader("📊 Summary Statistics")
st.write(df.describe())

st.subheader("💰 Average Price per Sqft by Locality")
st.bar_chart(df.groupby("Locality")["Price per Sqft (INR)"].mean())

st.subheader("📐 Built-up Area vs Estimated Sale Price")
st.scatter_chart(df[["Built-up Area (sqft)", "Estimated Sale Price (INR)"]])

st.subheader("🪑 Furnishing Status Distribution")
st.bar_chart(df["Furnishing Status"].value_counts())
``
