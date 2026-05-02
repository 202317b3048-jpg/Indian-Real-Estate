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
# Upload Dataset
# --------------------------------------------------
st.subheader("📂 Upload Real Estate Dataset")

uploaded_file = st.file_uploader(
    "Upload 'Real_estate_data_India 2.xlsx'",
    type=["xlsx"]
)

if uploaded_file is None:
    st.info("Please upload the Excel file to continue.")
    st.stop()

# --------------------------------------------------
# Load Excel Safely
# --------------------------------------------------
@st.cache_data
def load_data(file):
    return pd.read_excel(
        file,
        sheet_name="Raw data",
        engine="openpyxl"   # Explicit engine
    )

try:
    df = load_data(uploaded_file)
except ImportError:
    st.error(
        "❌ Missing dependency: openpyxl.\n\n"
        "✅ Fix: Add **openpyxl** to requirements.txt"
    )
    st.stop()
except Exception as e:
    st.error(f"❌ Unable to read Excel file: {e}")
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

