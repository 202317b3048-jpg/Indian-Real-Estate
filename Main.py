import streamlit as st
import pandas as pd

st.set_page_config(page_title="Madurai Real Estate Dashboard", layout="wide")
st.title("🏠 Madurai Real Estate Market Dashboard")

# Load Excel file
@st.cache_data
def load_data():
    return pd.read_excel("Madurai_RealEstate_Data (1).xlsx", engine="openpyxl")

df = load_data()

# Data preview
st.subheader("📄 Dataset Preview")
st.dataframe(df)

# Summary statistics
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# =========================
# Average Price per Sqft by Locality
# =========================
st.subheader("💰 Average Price per Sqft by Locality")

price_locality = df.groupby("Locality")["Price per Sqft (INR)"].mean()
st.bar_chart(price_locality)

# =========================
# Built-up Area vs Sale Price
# =========================
st.subheader("📐 Built-up Area vs Estimated Sale Price")

scatter_data = df[["Built-up Area (sqft)", "Estimated Sale Price (INR)"]]
st.scatter_chart(scatter_data)

# =========================
# Furnishing Status Distribution
# =========================
st.subheader("🪑 Furnishing Status Distribution")

furnishing_count = df["Furnishing Status"].value_counts()
st.bar_chart(furnishing_count)

# =========================
# Rental Yield by Locality
# =========================
st.subheader("📈 Average Rental Yield by Locality")

rental_yield = df.groupby("Locality")["Rental Yield (%)"].mean()
st.bar_chart(rental_yield)

# =========================
# Key Insights
# =========================
st.subheader("✅ Key Insights")
st.markdown("""
- Prices vary significantly across Madurai localities
- Larger built-up areas lead to higher sale prices
- Furnishing status impacts buyer interest
- Rental yield highlights good investment zones
""")
