import pandas as pd
import matplotlib.pyplot as plt

st.markdown("## 📈 City Price Comparison")

# Convert city price data to DataFrame
df_city = pd.DataFrame({
    "City": city_price.keys(),
    "Price per Sq.ft (₹)": city_price.values()
})

# Create bar chart
fig, ax = plt.subplots()
ax.bar(df_city["City"], df_city["Price per Sq.ft (₹)"])
ax.set_xlabel("City")
ax.set_ylabel("Price per Sq.ft (₹)")
ax.set_title("Average Base Property Price by City (India)")
plt.xticks(rotation=30)

# Display chart in Streamlit
st.pyplot(fig)
