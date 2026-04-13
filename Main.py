# Indian-Real-Estate
# what-if calculator for Indian Real Estate analyst  
import streamlit as st
 
st.title("simple streamlit app")
st.header("welcome")
st.write("this is a simple streamlit app")
 
name=st.text_input("enter your name")
if name:
    st.success(f"hello, {name}!  \nHow are you?")
 
number= st.slider("pick your age", 0, 100)
st.write(f"you age is {number}")
