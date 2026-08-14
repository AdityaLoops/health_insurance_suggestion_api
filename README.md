# Health Insurance Suggestion API

An end-to-end machine learning application that predicts estimated health insurance charges based on personal and demographic information.

## Project Status

🚧 **Backend Complete — Frontend In Progress**

The machine learning pipeline and FastAPI backend are complete, tested, and ready to be connected to a user-facing frontend.

## Dataset

The project uses the Medical Cost Personal Dataset containing 1,338 records.

### Features
- Age
- Sex
- BMI
- Number of children
- Smoking status
- Region

### Target
- Insurance charges

## Machine Learning

### Model Comparison

| Model | MAE | R² Score |
|---|---:|---:|
| Linear Regression | ~$4,181 | ~0.784 |
| **Random Forest** | **~$2,528** | **~0.864** |

Random Forest significantly outperformed the Linear Regression baseline and is currently used by the API.

### ML Pipeline

Dataset → Train/Test Split → ColumnTransformer → OneHotEncoder → Random Forest Regressor → Model Evaluation → Joblib Model

The preprocessing and model are combined into a single Scikit-learn Pipeline and saved with Joblib, ensuring the same preprocessing is applied during inference.

## Backend

The prediction service is built with FastAPI.

### API Endpoints

- `GET /` — API status and information
- `GET /health` — Health check
- `POST /predict` — Predict estimated insurance charges

### Prediction Flow

Client → POST /predict → Pydantic Validation → Pandas DataFrame → Saved ML Pipeline → Random Forest → Predicted Insurance Charge → JSON Response

### Example Request

`{"age":40,"sex":"male","bmi":30.0,"children":2,"smoker":"no","region":"northwest"}`

### Example Response

`{"predicted_charge":7140.83,"currency":"USD","model":"Random Forest Regressor"}`

The API uses Pydantic validation to reject invalid inputs before they reach the machine learning pipeline.

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Joblib
- FastAPI
- Uvicorn
- Pydantic

## Project Structure

health_insurance_suggestion_api/
├── insurance.csv
├── explore.py
├── train_model.py
├── main.py
├── .gitignore
└── venv/

## Current Features

- [x] Exploratory data analysis
- [x] Train/test split
- [x] Categorical feature encoding
- [x] Linear Regression baseline
- [x] Random Forest model
- [x] Model comparison
- [x] Scikit-learn Pipeline
- [x] Model persistence with Joblib
- [x] FastAPI backend
- [x] Pydantic input validation
- [x] Structured API responses
- [x] Swagger API testing
- [x] Edge-case and validation testing

## Planned Work

- [ ] Build user-facing frontend
- [ ] Connect frontend to FastAPI
- [ ] Improve UI/UX
- [ ] Deploy the complete application

## Disclaimer

This project is built for educational and demonstration purposes. Predicted charges are estimates generated from the training dataset and should not be considered actual insurance quotes or financial advice.