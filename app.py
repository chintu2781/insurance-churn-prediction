import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("churn_model.pkl")

st.title("Insurance Customer Churn Predictor")

# User inputs
age = st.slider("Age", 18, 90)
premium = st.slider("Monthly Premium", 100, 1000)
service_years = st.slider("Years with Company", 0, 20)
complaints = st.radio("Filed Complaints", ["Yes", "No"])

# Convert input
data = np.array([[age, premium, service_years, 1 if complaints == "Yes" else 0]])

# Predict button
if st.button("Predict"):
    result = model.predict(data)
    if result[0] == 1:
        st.error("Customer WILL CHURN")
    else:
        st.success("Customer WILL STAY")
