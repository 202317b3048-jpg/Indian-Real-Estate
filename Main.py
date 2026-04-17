import streamlit as st
import pandas as pd
st.title("Real Estate Market Analyzer  Madurai")
Sidebar selection
citie [ "Madural"]
selected city st.sidebar.selectbox("select a city:", cities)
Load dataset based on selection
def load data(city):
if city "Madurai":
return pd.read_csv("Madurai.csv")
#exact filename
show dataset
st.subheader("Dataset for (selected_city)")
st.dataframe(df)
Summary statistics
st.subheader("Summary Statistics")
 st.write(df.describe())
 
