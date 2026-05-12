import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("synthetic_water_data.csv")

X = df.values

model = IsolationForest(contamination=0.1)
model.fit(X)

print("Model trained successfully!")
