import streamlit as st
import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from joblib import dump, load

# ======================================
# Page Configuration
# ======================================
st.set_page_config(
    page_title="Madurai Property Price Prediction",
    layout="centered"
)

st.title("🏡 Madurai Property Price Prediction System")
st.caption("AI-powered real estate valuation using Machine Learning")

DATA_FILE = "madurai_property_data.csv"
DB_FILE = "properties.db"
MODEL_FILE = "price_model.pkl"

# ======================================
# Helper Functions
# ======================================
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame()

def save_to_db(df):
    conn = sqlite3.connect(DB_FILE)
    df.to_sql("properties", conn, if_exists="append", index=False)
    conn.close()

def train_model(df):
    df = df.copy()
    encoder = LabelEncoder()

    for col in ["Property Type", "Facing", "Furnishing", "Parking"]:
        df[col] = encoder.fit_transform(df[col])

    X = df[
        [
            "Built-up Area",
            "Price per Sqft",
            "Bedrooms",
            "Bathrooms",
            "Property Age",
            "Metro Distance",
            "IT Hub Distance",
            "Parking"
        ]
    ]
    y = df["Calculated Price"]

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )
    model.fit(X, y)
    dump(model, MODEL_FILE)
    return model

# ======================================
# Load data & model
# ======================================
df_existing = load_data()

model = None
if os.path.exists(MODEL_FILE):
    model = load(MODEL_FILE)

# ======================================
# Property Input Form
# ======================================
with st.form("property_form"):
    st.subheader("📋 Property Details")

    locality = st.text_input("Locality")
    property_type = st.selectbox(
        "Property Type",
        ["Apartment", "Independent House", "Villa", "Plot"]
    )

    built_up_area = st.number_input("Built-up Area (sqft)", min_value=100, step=10)
    price_sqft = st.number_input("Price per Sqft (INR)", min_value=500, step=100)
    bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
    bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])
    property_age = st.number_input("Property Age (years)", min_value=0)
    facing = st.selectbox("Facing", ["North", "South", "East", "West"])
    furnishing = st.selectbox(
        "Furnishing",
        ["Unfurnished", "Semi-Furnished", "Fully Furnished"]
    )
    parking = st.radio("Parking Facility", ["Yes", "No"])
    metro_distance = st.number_input("Metro Distance (km)", min_value=0.0)
    it_distance = st.number_input("IT Hub Distance (km)", min_value=0.0)
    buyer_score = st.slider("Buyer Attraction Score", 1, 10)

    submitted = st.form_submit_button("✅ Submit & Predict")

# ======================================
# Submission Logic (✅ ERROR FIXED HERE)
# ======================================
if submitted:
    calculated_price = built_up_area * price_sqft

    # ✅ Properly closed dictionary
    new_data = {
        "Locality": locality,
        "Property Type": property_type,
        "Built-up Area": built_up_area,
        "Price per Sqft": price_sqft,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Property Age": property_age,
        "Facing": facing,
        "Furnishing": furnishing,
        "Parking": parking,
        "Metro Distance": metro_distance,
        "IT Hub Distance": it_distance,
        "Buyer Score": buyer_score,


