import serial
import numpy as np
import pandas as pd
import time
from sklearn.ensemble import RandomForestClassifier

# 🔹 LOAD DATA
df = pd.read_csv("synthetic_water_data.csv")

# 🔹 FEATURES (same as before but explicit)
X = df[["flow", "pressure", "tds", "vibration"]]

# 🔹 TARGET (must exist in CSV)
y = df["action"]   # FULL / HALF / QUAT

# 🔹 TRAIN MODEL
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

print("✅ RandomForest model trained. Starting system...")

# 🔹 STATE VARIABLES
current_state = "FULL"   # initial assumed position

time.sleep(2)  # allow Arduino to settle

# 🔁 MAIN LOOP
while True:
    line = ser.readline().decode().strip()

    if line:
        try:
            values = line.split(",")

            if len(values) == 6:
                flow = float(values[0])
                pressure = float(values[1])
                temp = float(values[2])
                tds = float(values[3])
                ph = float(values[4])
                vibration = float(values[5])

                # 🔹 PRINT LIVE DATA
                print(f"Flow: {flow:.2f} | Pressure: {pressure:.0f} | "
                      f"TDS: {tds:.0f} | pH: {ph:.2f} | Vib: {vibration:.3f}")

                # 🔹 ML PREDICTION
                sample = np.array([[flow, pressure, tds, vibration]])
                prediction = model.predict(sample)[0]

                command = None

                command = prediction

                print(f"🤖 ML Decision → {command}")

                # 🔥 SEND COMMAND ONLY IF STATE CHANGES
                if command is not None and command != current_state:
                    ser.write((command + "\n").encode())
                    print(f"➡️ Command Sent: {command}")
                    current_state = command

        except Exception as e:
            print("Parse error:", line)

    time.sleep(0.1)  # prevents serial flooding
