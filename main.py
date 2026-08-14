import joblib
from fastapi import FastAPI, HTTPException
import pandas as pd
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(
    title = "Health Insurance Suggestion API",
    description = "API for prediction health insurance charges using a trained Random Forest Regressor model",
    version ="1.0.0"
)

model = joblib.load("insurance_model.joblib")

class InsuranceFeatures(BaseModel):
    age: int = Field(gt=0, le=110, description="Age of the individual")
    sex: Literal["male", "female"] = Field(description ="Sex of the individual")
    bmi: float = Field(gt=15, le=54, description="Body Mass Index of the individual")
    children: int = Field(ge=0, le=5, description="Number of children of the individual")
    smoker: Literal["yes", "no"] = Field(description="Is the individual a smoker?")
    region: Literal["southwest", "southeast", "northwest", "northeast"] = Field(description="Region of the individual")


@app.get("/")
def home():
    return {"message": "Health Insurance Suggestion API",
            "status": "running",
            "docs" : "/docs"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": "Random forest Regressor",
        "model loaded": True
    }

@app.post("/predict")
def predict(features: InsuranceFeatures):
    input_data = pd.DataFrame([features.model_dump()])
    prediction = model.predict(input_data)[0]
    return {
        "predicted charge": round(float(prediction),2)
    }
