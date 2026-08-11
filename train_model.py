import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error, r2_score
# this transformer will help us to apply one hot encoding to categorical columns and leave the numerical
# columns as it is. We will use this transformer in our pipeline

df = pd.read_csv("insurance.csv")

x = df.drop("charges", axis = 1)
# or  x = df.drop(columns=["charges"])
y = df["charges"]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

encoder = OneHotEncoder(handle_unknown="ignore")

# x_train_encoded = encoder.fit_transform(x_train).ColumnTransformer("sex", "smoker", "region")     WRONG

preprocessor = ColumnTransformer( [(" categorical" ,encoder, ["sex", "smoker", "region"])], remainder="passthrough")

x_train_encoded = preprocessor.fit_transform(x_train)
x_test_encoded = preprocessor.transform(x_test)
# we used only TRANSFORM on x_test bc the encoder has learned the encoding from the training data .
# we don't want to fit the encoder again on x_test.

model = LinearRegression()
model.fit(x_train_encoded, y_train)

y_pred = model.predict(x_test_encoded)

mae = mean_absolute_error(y_test, y_pred)
r2= r2_score(y_test, y_pred)

print(f"MAE: {mae}")
print(f"R2: {r2}")

# CHECK FOR OVERFITTING 
train_pred = model.predict(x_train_encoded)
train_r2 = r2_score(y_train, train_pred)
test_r2 = r2_score(y_test, y_pred)

print(f"Train R2: {train_r2:.4f}")
print(f"Test R2: {test_r2:.4f}")


