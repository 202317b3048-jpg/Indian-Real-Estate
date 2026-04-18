import streamlit as st

# Page configuration
st.set_page_config(page_title="Madurai Dashboard", layout="centered")

# Title
st.title("📍 Madurai, Tamil Nadu")

# Subtitle
st.subheader("Cultural Capital of Tamil Nadu")

# Basic description
st.write(
    """
Madurai is one of the oldest continuously inhabited cities in India.
It is famous for the **Meenakshi Amman Temple**, rich Tamil culture,
and vibrant street life.
"""
)

# Key information
st.markdown("### 🧭 Quick Facts")
st.write("- **State:** Tamil Nadu")
st.write("- **Region:** Southern Tamil Nadu")
st.write("- **Known for:** Temples, textiles, jasmine flowers")

# Location coordinates
st.markdown("### 📌 Location on Map")
madurai_lat = 9.9252
madurai_lon = 78.1198

st.map(
    [{"lat": madurai_lat, "lon": madurai_lon}]
)

# Simple interaction
st.markdown("### 💬 Say Hello")
name = st.text_input("Enter your name")

if name:
    st.success(f"Vanakkam, {name}! Welcome to Madurai 🙏")
