import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="India Property Price Estimator",
    layout="centered"
)

st.title("🏢 India Property Price Estimator")
st.caption("Estimate property value using India real estate market data")

# --------------------------------------------------
# Load Dataset (SAFE + ERROR HANDLING)
# --------------------------------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_excel(
            "Real_estate_data_India 2.xlsx",
            sheet_name="Raw data"
        )
        return df
    except FileNotFoundError:
        st.error("❌ Excel file not found. Please ensure 'Real_estate_data_India 2.xlsx' is in the app folder.")
        return None
    except ValueError:
        st.error("❌ Sheet name 'Raw data' not found. Please check the Excel sheet name.")
        return None
    except ImportError:
        st.error("❌ Missing dependency: openpyxl. Please install it or add it to requirements.txt.")
        return None
    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")
        return None


df = load_data()

if df is None:
    st.stop()

# --------------------------------------------------
# Location Selection
# --------------------------------------------------
st.subheader("📍 Location Details")

state = st.selectbox(
    "State / Union Territory",
    sorted(df["State / Union Territory"].dropna().unique())
)

state_df = df[df["State / Union Territory"] == state]

city = st.selectbox(
    "City",
    sorted(state_df["City"].dropna().unique())
)

city_row = state_df[state_df["City"] == city].iloc[0]

# Extract values safely
market_tier = city_row["Market Tier"]
price_per_sqft = float(city_row["Price/sqft (₹)"])
median_price_2025 = city_row["Median House Price (₹ Lakh) -2025"]
yoy_growth = float(city_row["YoY Price Growth (%)"])
cagr_5y = float(city_row["5-Year CAGR (%)"])

st.info(
    f"""
**Market Tier:** {market_tier}  
**Avg Price / Sqft:** ₹{price_per_sqft:,.0f}  
**Median House Price (2025):** ₹{median_price_2025} Lakh  
"""
)

# --------------------------------------------------
