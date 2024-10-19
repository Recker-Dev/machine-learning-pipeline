import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import mlflow
import os

# Set up DagsHub as the tracking URI
os.environ['MLFLOW_TRACKING_URI']="https://dagshub.com/Recker-Dev/machine-learning-pipeline.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME']="Recker-Dev"
os.environ["MLFLOW_TRACKING_PASSWORD"]="5a116545c06e17b9da861c6ee79dcb79032d2510"

# Load the trained model
model = pickle.load(open('models/model.pkl', 'rb'))

# Initialize FastAPI app
app = FastAPI()

# Define a class for input features
class ModelInput(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float



@app.get('/')
def index():
    return {'message': 'Hello Everyone '}

# Define an endpoint for prediction
@app.post("/predict")
def predict(input_data: ModelInput):
    # Convert input data to pandas DataFrame
    data = pd.DataFrame([input_data.dict()])

    # Make a prediction
    prediction = model.predict(data)

    # Log prediction with MLflow
    mlflow.log_metric("prediction", int(prediction[0]))

    # Return the prediction result
    return {"Prediction": int(prediction[0])}

# Run the FastAPI app with:
# uvicorn app:app --reload
