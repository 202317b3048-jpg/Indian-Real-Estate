import streamlit as st
import pandas as pd

st.title("Real Estate Market Analyzer Vijayawada & Madurai")

#Sidebar selection
cities = ["Vijayawada", "Madurai"]
selected_city = st.sidebar.selectbox("Select a city:", cities)

#Load dataset based on selection
def load_data(city):
    if city == "Vijayawada":
 return pd.read_csv("Vijayawada.csv") #exact filename
    else:
       return pd.read_csv("Madurai.csv") #exact filename
 df =  load_data(selected_city)
 #Show dataset
st.subheader(f"Dataset for (selected_city)")
st.dataframe(df)

#Summary statistics
st.subheader("Summary Statiics")
st.write(df.describe())
 
