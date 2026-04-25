import streamlit as st
import pandas as pd
import sqlite3
import os
import joblib
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# =====================================================
# Page Config
# =====================================================
st.set_page_config(page_title="Madurai Property AI", layout="centered")
st.title("🏡 Madurai Property Price AI Dashboard")
st.caption("ML-powered property analytics & price prediction")

DATA_FILE = "madurai_property_data.csv"
DB_FILE = "properties.db"
MODEL_FILE = "price_model.pkl"

# =====================================================
# Utility Functions
# =====================================================
@st.cache_data
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

    for col in ["Property Type", "Furnishing", "Facing", "Parking"]:
        df[col] = encoder.fit_transform(df[col])

    X = df[
        [
            "Built-up Area (sqft)",
            "Price per Sqft",
            "Bedrooms",
            "Bathrooms",
            "Property Age",
            "Metro Distance (km)",
            "IT Hub Distance (km)",
            "Parking"
        ]
    ]
    y = df["Calculated Price"]

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X, y)
    joblib.dump(model, MODEL_FILE)
    return model

# =====================================================
# Load Existing Data & Model
# =====================================================
df_existing = load_data()
model = joblib.load(MODEL_FILE) if os.path.exists(MODEL_FILE) else None

# =====================================================
# Property Input Form
# =====================================================
with st.form("property_form"):
    st.subheader("📋 Property Details")

    locality = st.text_input("Locality")
    property_type = st.selectbox("Property Type", ["Apartment", "Independent House", "Villa", "Plot"])
    built_up_area = st.number_input("Built-up Area (sqft)", min_value=100, step=10)
    price_per_sqft = st.number_input("Price per Sqft (INR)", min_value=500, step=100)
    bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
    bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])
    property_age = st.number_input("Property Age (years)", min_value=0)
    facing = st.selectbox("Facing", ["North", "South", "East", "West"])
    furnishing = st.selectbox("Furnishing", ["Unfurnished", "Semi-Furnished", "Fully Furnished"])
    parking = st.radio("Parking", ["Yes", "No"])
    distance_metro = st.number_input("Metro Distance (km)", min_value=0.0)
    distance_it = st.number_input("IT Hub Distance (km)", min_value=0.0)
    maintenance = st.number_input("Monthly Maintenance", min_value=0)
    buyer_score = st.slider("Buyer Attraction Score", 1, 10)

    submit = st.form_submit_button("✅ Submit & Predict")

# =====================================================
# Submission Logic
# =====================================================
if submit:
    calculated_price = built_up_area * price_per_sqft

    new_data = {
        "Locality": locality,
        "Property Type": property_type,
        "Built-up Area (sqft)": built_up_area,
        "Price per Sqft": price_per_sqft,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Property Age": property_age,
        "Facing": facing,
        "Furnishing": furnishing,
        "Parking": parking,
        "Metro Distance (km)": distance_metro,
        "IT Hub Distance (km)": distance_it,
        "Maintenance": maintenance,
        "Buyer Score": buyer_score,
        "Calculated Price": calculated_price,
    }

    df_new = pd.DataFrame([new_data])
    df_all = pd.concat([df_existing, df_new], ignore_index=True)

    # Save
    df_all.to_csv(DATA_FILE, index=False)
    save_to_db(df_new)

    # Train model if needed
    model = train_model(df_all)

    # Prediction
    parking_val = 1 if parking == "Yes" else 0
    predicted_price = model.predict([[
        built_up_area,
        price_per_sqft,
        bedrooms,
        bathrooms,
        property_age,
        distance_metro,
        distance_it,
        parking_val
    ]])[0]

    st.success("✅ Property Saved Successfully!")

    st.subheader("🤖 ML Price Prediction")
    st.metric("Predicted Market Price", f"₹{predicted_price:,.0f}")
    st.metric("Calculated Price", f"₹{calculated_price:,.0f}")

# =====================================================
# Charts & Analytics
# =====================================================
if not df_existing.empty:
    st.subheader("📊 Locality-wise Price Trends")

    
