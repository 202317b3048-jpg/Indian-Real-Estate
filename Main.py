import streamlit as st
import pandas as pd
import sqlite3
import os


from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from joblib import dump, load

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Madurai Property AI",
    layout="centered"
)

st.title("🏡 Madurai Property Price Prediction System")
st.caption("ML‑based real‑estate analytics dashboard")

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
    st.subheader("📋 Property Details")

    locality = st.text_input("Locality")
    property_type = st.selectbox(
        "Property Type",
        ["Apartment", "Independent House", "Villa", "Plot"]
    )
    built_up_area = st.number_input(
        "Built-up Area (sqft)", min_value=100, step=10
    )
    price_sqft = st.number_input(
        "Price per Sqft (INR)", min_value=500, step=100
    )
    bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
    bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])
    property_age = st.number_input("Property Age (Years)", min_value=0)
    facing = st.selectbox("Facing", ["North", "South", "East", "West"])
    furnishing = st.selectbox(
        "Furnishing",
        ["Unfurnished", "Semi-Furnished", "Fully Furnished"]
    )
    parking = st.radio("Parking Facility", ["Yes", "No"])
    metro_distance = st.number_input("Metro Distance (km)", min_value=0.0)
    it_distance = st.number_input("IT Hub Distance (km)", min_value=0.0)
    buyer_score = st.slider("Buyer Attraction Score", 1, 10)

    submitted = st.form_submit_button("✅ Submit & Predict Price")

# =====================================================
# SUBMISSION & PREDICTION
# =====================================================
if submitted:
    calculated_price = built_up_area * price_sqft

    row = {
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
        "Calculated Price": calculated_price
    }

    df_new = pd.DataFrame([row])
    df_all = pd.concat([df_existing, df_new], ignore_index=True)

    df_all.to_csv(DATA_FILE, index=False)
    save_to_db(df_new)

    model = train_model(df_all)

    parking_val = 1 if parking == "Yes" else 0

    predicted_price = model.predict([[
        built_up_area,
        price_sqft,
        bedrooms,
        bathrooms,
        property_age,
        metro_distance,
        it_distance,
        parking_val
    ]])[0]

    st.success("✅ Property data saved successfully!")

    st.subheader("🤖 AI Price Prediction")
    st.metric("Predicted Market Price", f"₹{predicted_price:,.0f}")
    st.metric("Calculated Price", f"₹{calculated_price:,.0f}")

# =====================================================
# CHARTS & ANALYTICS
# =====================================================
if not df_existing.empty:
    st.subheader("📊 Average Price by Locality")
    avg_price = df_existing.groupby("Locality")["Calculated Price"].mean()

    fig, ax = plt.subplots()
    avg_price.plot(kind="bar", ax=ax)
    ax.set_xlabel("Locality")
