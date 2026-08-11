import  pandas as pd

df = pd.read_csv("insurance.csv")
print(df.shape)
print(df.head())
print(df.tail())
print(df.describe())
print(df.isnull().sum())
print(df.dtypes)

print(df.groupby("smoker")["charges"].mean())
print(df.corr(numeric_only=True)["charges"].sort_values(ascending=False))