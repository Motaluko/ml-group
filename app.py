import streamlit as st
import joblib
import numpy as np
import os

MODEL_PATH = "house_price_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error(f"Model file not found: {MODEL_PATH}. Upload it to the project folder.")
    st.stop()

model = joblib.load(MODEL_PATH)

st.title("California House Price Prediction")

st.write("Enter the house features below:")

# Input fields
MedInc = st.number_input("Median Income", min_value=0.0)
HouseAge = st.number_input("House Age", min_value=0.0)
AveRooms = st.number_input("Average Rooms", min_value=0.0)
AveBedrms = st.number_input("Average Bedrooms", min_value=0.0)
Population = st.number_input("Population", min_value=0.0)
AveOccup = st.number_input("Average Occupancy", min_value=0.0)
Latitude = st.number_input("Latitude", min_value=-90.0)
Longitude = st.number_input("Longitude", min_value=-180.0)

if st.button("Predict"):
    try:
        features = [
            MedInc, HouseAge, AveRooms, AveBedrms,
            Population, AveOccup, Latitude, Longitude
        ]

        pred = model.predict([features])[0]
        predicted_price = pred * 100000

        st.success(f"Predicted median house value: ${predicted_price:,.2f}")

    except Exception as e:
        st.error("An error occurred while predicting. Please check your inputs.")
