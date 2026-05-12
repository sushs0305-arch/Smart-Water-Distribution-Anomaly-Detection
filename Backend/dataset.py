import numpy as np
import pandas as pd

np.random.seed(42)

# NORMAL DATA
normal_flow = np.random.normal(70, 5, 100)
normal_pressure = np.random.normal(100500, 200, 100)
normal_tds = np.random.normal(300, 50, 100)
normal_vibration = np.random.normal(0.02, 0.01, 100)

normal_data = np.column_stack((normal_flow, normal_pressure, normal_tds, normal_vibration))

# ANOMALIES
anomaly_flow = np.random.normal(150, 10, 20)
anomaly_pressure = np.random.normal(90000, 500, 20)
anomaly_tds = np.random.normal(800, 100, 20)
anomaly_vibration = np.random.normal(0.3, 0.1, 20)

anomaly_data = np.column_stack((anomaly_flow, anomaly_pressure, anomaly_tds, anomaly_vibration))

# Combine
data = np.vstack((normal_data, anomaly_data))

df = pd.DataFrame(data, columns=["flow", "pressure", "tds", "vibration"])
df.to_csv("synthetic_water_data.csv", index=False)

print("Dataset created!")
