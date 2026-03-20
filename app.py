import streamlit as st
import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open("model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Delivery Time Predictor", page_icon="🚚")

# Title
st.title("🚚 Delivery Time Prediction")
st.write("Enter shipment details below to predict the estimated delivery time.")

st.divider()

# --- Input Fields ---
col1, col2 = st.columns(2)

with col1:
    product_category = st.selectbox("Product Category", ["Furniture", "Electronics", "Clothing"])
    warehouse = st.selectbox("Warehouse Location", ["Mumbai", "Delhi", "Hyderabad", "Pune", "Bangalore"])
    shipment_mode = st.selectbox("Shipment Mode", ["Sea", "Road", "Air"])

with col2:
    weight = st.number_input("Product Weight (kg)", min_value=0.1, value=5.0, step=0.1)
    demand = st.number_input("Demand Forecast (units)", min_value=1.0, value=100.0, step=1.0)
    cost = st.number_input("Shipping Cost (₹)", min_value=0.0, value=50.0, step=0.5)

st.divider()

# --- Predict Button ---
if st.button("🔮 Predict Delivery Time"):
    data = pd.DataFrame({
        "Product_Category": [product_category],
        "Warehouse_Location": [warehouse],
        "Product_Weight_kg": [weight],
        "Shipment_Mode": [shipment_mode],
        "Demand_forecast_units": [demand],
        "Shipping_Cost": [cost]
    })

    prediction = model.predict(data)
    st.success(f"📦 Estimated Delivery Time: **{round(prediction[0], 2)} days**")
