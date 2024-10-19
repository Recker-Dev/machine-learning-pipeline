import streamlit as st
import requests
import pandas as pd

# FastAPI URL 
API_URL = "http://127.0.0.1:8000/predict"

# App title
st.title("Customer Diabetes Prediction Web App")

# Fields for user input based on your data
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=85)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=122, value=72)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=35)
insulin = st.number_input("Insulin", min_value=0, max_value=846, value=0)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=28.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.627)
age = st.slider("Age", min_value=10, max_value=100, value=50)

# When the user clicks the 'Predict' button
if st.button('Predict'):
    # Prepare data for the API request (as JSON)
    input_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }
    
    # Send POST request to FastAPI and get response
    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            prediction = response.json()["Prediction"]

            # Display the result
            if prediction == 1:
                st.error("The model predicts that the person is likely to have diabetes.")
            else:
                st.success("The model predicts that the person is unlikely to have diabetes.")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"Error making request: {e}")
