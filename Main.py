import streamlit as st
import pandas as pd

st.title("Real Estate Market Analyzer – Madurai")

# Load Madurai dataset
@st.cache_data
def load_data():
    return pd.read_csv("Madurai.csv")  # exact filename

df = load_data()

# Show dataset
st.subheader("Dataset for Madurai")
st.dataframe(df)

# Summary statistics
st.subheader("Summary Statistics")
st.write(df.describe())
 
