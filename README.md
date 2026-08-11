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