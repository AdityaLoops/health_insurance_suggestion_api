import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline 
# this transformer will help us to apply one hot encoding to categorical columns and leave the numerical
# columns as it is. We will use this transformer in our pipeline

df = pd.read_csv("insurance.csv")

x = df.drop("charges", axis = 1)
# or  x = df.drop(columns=["charges"])
y = df["charges"]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

encoder = OneHotEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer( [(" categorical" ,encoder, ["sex", "smoker", "region"])], remainder="passthrough")

model = RandomForestRegressor(n_estimators=200, random_state=42)
pipeline = Pipeline([("preprocessor", preprocessor), ("model", model)])
pipeline.fit(x_train, y_train)
y_pred = pipeline.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MAE: {mae}")
print(f"R2: {r2}")


joblib.dump(pipeline, "insurance_model.joblib")
print("Model saved as insurance_model.joblib")
