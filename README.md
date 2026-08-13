# Health Insurance Suggestion API

A machine learning project that predicts estimated health insurance charges based on personal and demographic information.

## Project Status

🚧 **In Development**

The machine learning pipeline is currently being built. The first baseline model using Linear Regression has been trained and evaluated.

## Dataset

The project uses the Medical Cost Personal Dataset.

Features:

- Age
- Sex
- BMI
- Number of children
- Smoking status
- Region

Target:

- Insurance charges

The dataset contains 1,338 records.

## Current ML Pipeline

```text
Dataset
   ↓
Exploratory Data Analysis
   ↓
Train/Test Split
   ↓
Categorical Feature Encoding
   ↓
Linear Regression
   ↓
Model Evaluation
```

## Current Results

### Linear Regression Baseline

- MAE: ~$4,181
- R² Score: ~0.784

### Random Forest

- MAE: ~$2,528
- R² Score: ~0.864

Random Forest significantly improves upon the Linear Regression baseline, reducing the average error while explaining more variation in insurance charges.

The Random Forest model currently performs best on the test set.

## Tech Stack

- Python
- Pandas
- Scikit-learn
- Joblib
- FastAPI
- Uvicorn
- Pydantic

## Project Structure

```text
health_insurance_suggestion_api/
├── insurance.csv
├── explore.py
├── train_model.py
├── main.py
├── .gitignore
└── venv/
```

## Planned Work

- [x] Compare Linear Regression with Random Forest
- [ ] Select and save the final model
- [ ] Build the FastAPI prediction endpoint
- [ ] Add Pydantic input validation
- [ ] Test the API
- [ ] Add API documentation
- [ ] Improve README with final results
- [ ] Deploy the API

 