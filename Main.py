import streamlit as st
import pandas as pd

st.set_page_config(page_title="Madurai Real Estate", layout="wide")

st.title("🏡 Madurai Real Estate Dashboard")

@st.cache_data
def load_data():
    return pd.read_excel("madurai_real_estate.xlsx")

df = load_data()

st.subheader("Property Data")
st.dataframe(df)

st.subheader("📊 Average Price per Sqft by Locality")
st.bar_chart(df.groupby("Locality")["Price per Sqft (INR)"].mean())


   
