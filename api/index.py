import joblib
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel, Field
from typing import Literal
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

app = FastAPI(
    title="Health Insurance Suggestion API",
    description="API for predicting health insurance charges using a trained Random Forest Regressor model.",
    version="1.0.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
BASE_DIR  = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR/"insurance_model.joblib")

class InsuranceFeatures(BaseModel):
    age: int = Field(gt=0, le=110, description="Age of the individual")
    sex: Literal["male", "female"] = Field(description ="Sex of the individual")
    bmi: float = Field(gt=15, le=54, description="Body Mass Index of the individual")
    children: int = Field(ge=0, le=5, description="Number of children of the individual")
    smoker: Literal["yes", "no"] = Field(description="Is the individual a smoker?")
    region: Literal["southwest", "southeast", "northwest", "northeast"] = Field(description="Region of the individual")

class PredictionResponse(BaseModel):
    predicted_charge: float
    currency: str
    model: str

@app.get("/api/")
def home():
    return {"message": "Health Insurance Suggestion API",
            "status": "running",
            "docs" : "/api/docs"}

@app.get("/api/health")
def health():
    return {
        "status": "healthy",
        "model": "Random forest Regressor",
        "model_loaded": True
    }
# output format
@app.post("/api/predict", response_model=PredictionResponse) 
# input format
def predict(features: InsuranceFeatures):
    input_data = pd.DataFrame([features.model_dump()])
    prediction = model.predict(input_data)[0]
    return {
        "predicted_charge": round(float(prediction),2),
        "currency": "USD",
        "model": "Random Forest Regressor"
    }
