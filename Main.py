import streamlit as st
import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from joblib import dump, load

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Madurai Property Price Prediction",
    layout="centered"
)

st.title("🏡 Madurai Property Price Prediction System")
st.caption("AI-powered real estate analytics using Machine Learning")

DATA_FILE = "madurai_property_data.csv"
DB_FILE = "properties.db"
MODEL_FILE = "price_model.pkl"

# =====================================================
# HELPER FUNCTIONS
# =====================================================
def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame()

def save_to_sqlite(df):
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

# =====================================================
# LOAD DATA & MODEL
# =====================================================
df_existing = load_data()

model = None
if os.path.exists(MODEL_FILE):
    model = load(MODEL_FILE)

# =====================================================
# PROPERTY INPUT FORM
# =====================================================
with st.form("property_form"):
    st.subheader("📋 Enter Property Details")

    locality = st.text_input("Locality (e.g., Anna Nagar, KK Nagar)")
    property_type = st.selectbox(
        "Property Type",
        ["Apartment", "Independent House", "Villa", "Plot"]
    )

    built_up_area = st.number_input(
        "Built-up Area (sqft)", min_value=100, step=10
    )

    price_per_sqft = st.number_input(
        "Price per Sqft (INR)", min_value=500, step=100
    )

    bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
    bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])
    property_age = st.number_input("Property Age (Years)", min_value=0)

    facing = st.selectbox("Facing", ["North", "South", "East", "West"])
    furnishing = st.selectbox(
        "Furnishing Status",
        ["Unfurnished", "Semi-Furnished", "Fully Furnished"]
    )

    parking = st.radio("Parking Facility", ["Yes", "No"])
    metro_distance = st.number_input("Distance to Metro (km)", min_value=0.0)
    it_distance = st.number_input("Distance to IT Hub (km)", min_value=0.0)

    buyer_score = st.slider("Buyer Attraction Score (1–10)", 1, 10)

    submitted = st.form_submit_button("✅ Submit & Predict")

# =====================================================
# SUBMISSION & ML PREDICTION
# =====================================================
if submitted:
    calculated_price = built_up_area * price_per_sqft

    new_data = {
        "Locality": locality,

