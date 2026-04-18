import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Madurai Real Estate Dashboard", layout="wide")

st.title("🏠 Madurai Real Estate Market Dashboard")

# Load Excel file
@st.cache_data
def load_data():
    return pd.read_excel("Madurai_RealEstate_Data (1).xlsx", engine="openpyxl")

df = load_data()

# =============================
# DATA PREVIEW
# =============================
st.subheader("📄 Dataset Preview")
st.dataframe(df)

# =============================
# SUMMARY STATISTICS
# =============================
st.subheader("📊 Summary Statistics")
st.write(df.describe())

# =============================
# PRICE PER SQFT BY LOCALITY
# =============================
st.subheader("💰 Average Price per Sqft by Locality")

price_locality = df.groupby("Locality")["Price per Sqft (INR)"].mean()

fig1, ax1 = plt.subplots()
price_locality.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Price per Sqft (INR)")
ax1.set_xlabel("Locality")
ax1.set_title("Average Price per Sqft by Locality")
plt.xticks(rotation=45)

st.pyplot(fig1)

# =============================
# BUILT-UP AREA VS SALE PRICE
# =============================
st.subheader("📐 Built-up Area vs Estimated Sale Price")

fig2, ax2 = plt.subplots()
ax2.scatter(
    df["Built-up Area (sqft)"],
    df["Estimated Sale Price (INR)"]
)
ax2.set_xlabel("Built-up Area (sqft)")
ax2.set_ylabel("Estimated Sale Price (INR)")
ax2.set_title("Built-up Area vs Estimated Sale Price")

st.pyplot(fig2)

# =============================
# PROPERTY COUNT BY FURNISHING
# =============================
st.subheader("🪑 Property Count by Furnishing Status")

furnishing_count = df["Furnishing Status"].value_counts()

fig3, ax3 = plt.subplots()
furnishing_count.plot(kind="pie", autopct="%1.1f%%", ax=ax3)
ax3.set_ylabel("")
ax3.set_title("Furnishing Status Distribution")

st.pyplot(fig3)

# =============================
# RENTAL YIELD BY LOCALITY
# =============================
st.subheader("📈 Average Rental Yield by Locality")

rental_yield = df.groupby("Locality")["Rental Yield (%)"].mean()

fig4, ax4 = plt.subplots()
rental_yield.plot(kind="barh", ax=ax4)
ax4.set_xlabel("Rental Yield (%)")
ax4.set_title("Average Rental Yield by Locality")

st.pyplot(fig4)

# =============================
# BUYER ATTRACTION SCORE
# =============================
st.subheader("⭐ Buyer Attraction Score Distribution")

fig5, ax5 = plt.subplots()
ax5.hist(df["Buyer Attraction Score (1-10)"], bins=10)
ax5.set_xlabel("Buyer Attraction Score")
ax5.set_ylabel("Number of Properties")
ax5.set_title("Buyer Attraction Score Distribution")

st.pyplot(fig5)

# =============================
# INSIGHTS
# =============================
st.subheader("✅ Key Insights")
st.markdown("""
- Price varies significantly by **locality**
- Larger built-up areas strongly increase **sale price**
- **Fully-furnished** houses form a major share
- Some localities offer **higher rental yield**, ideal for investors
- Buyer Attraction Score helps identify **high-demand areas**
""")
