import requests

# Define the URL of the FastAPI model serving endpoint
url = "http://127.0.0.1:8000/predict"

# Create a dictionary with input data for prediction
data = {
    "Pregnancies": 2,
    "Glucose": 148,
    "BloodPressure": 72,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.627,
    "Age": 50
}

# Send a POST request to the model serving endpoint
response = requests.post(url, json=data)

# Check the response status and print the result
if response.status_code == 200:
    print("Prediction response:", response.json())
else:
    print("Error:", response.status_code, response.text)
