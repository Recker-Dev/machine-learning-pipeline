import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

#### Get the  model

with open('models/model.pkl', 'rb') as file:
    model = pickle.load(file)





## App title

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


feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']


# When the user clicks the 'Predict' button
if st.button('Predict'):
    # Create a DataFrame with user input, using the correct feature names
    input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]], 
                              columns=feature_names)
    
    # Predict the outcome using the loaded model
    prediction = model.predict(input_data)
    
    # Display the result
    if prediction[0] == 1:
        st.error("The model predicts that the person is likely to have diabetes.")
    else:
        st.success("The model predicts that the person is unlikely to have diabetes.")