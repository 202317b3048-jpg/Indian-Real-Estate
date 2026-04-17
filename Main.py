import streamlit as st
import pandas as pd
st.title("Real Estate Market Analyzer Vijayawada & Madural")
Sidebar selection
cities ["Vijayawada", "Madural"]
selected city st.sidebar.selectbox("select a city:", cities)
Load dataset based on selection
def load data(city):
if city "Vijayawada":
return pd.read_csv("Vijayawada.csv")
#exact filename
elser
return pd.read_csv("Madurai.csv")
exact filename
df load data(selected_city)
show dataset
st.subheader("Dataset for (selected_city)")
st.dataframe(df)
Summary statistics
st.subheader("Summary Statistics")
st.write(df.describe())
 
 
