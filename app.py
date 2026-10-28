
from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI(
    title="Titanic Survival Prediction API",
    description="ML Model Serving using FastAPI",
    version="1.0"
)

# Load trained model
model = joblib.load("model.pkl")


# Input data validation
class Passenger(BaseModel):

    Pclass: int = Field(ge=1, le=3)
    Sex: str
    Age: float = Field(ge=0, le=100)
    SibSp: int = Field(ge=0)
    Parch: int = Field(ge=0)
    Fare: float = Field(ge=0)
    Embarked: str


# Health endpoint
@app.get("/health")
def health():

    return {
        "status": "API is running"
    }


# Prediction endpoint
@app.post("/predict")
def predict(passenger: Passenger):

    # Convert input into dataframe
    data = pd.DataFrame([passenger.model_dump()])

    # Generate prediction
    prediction = model.predict(data)

    # Return result
    if prediction[0] == 1:
        result = "Survived"
    else:
        result = "Not Survived"

    return {
        "prediction": result,
        "survived": int(prediction[0])
    }
