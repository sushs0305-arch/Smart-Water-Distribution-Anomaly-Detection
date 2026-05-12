import serial
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import time

# 🔹 SERIAL CONFIG (CHANGE PORT)
ser = serial.Serial('COM11', 9600, timeout=1)

# 🔹 LOAD + TRAIN MODEL (synthetic dataset)
df = pd.read_csv("synthetic_water_data.csv")
X = df[["flow", "pressure", "tds", "vibration"]].values

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

print("✅ Model trained. Starting intelligent control system...")

# 🔹 STATE TRACKING
current_state = "FULL"   # assume starting closed

time.sleep(2)  # allow Arduino reset

# 🔁 MAIN LOOP
while True:
    raw = ser.readline()
    line = raw.decode(errors='ignore').strip()

    if not line:
        continue

    # ignore garbage lines
    if "," not in line:
        print("⚠️ Skipping:", line)
        continue

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

                print(f"\n📡 Data → Flow:{flow:.2f}, Pressure:{pressure:.0f}, "
                      f"TDS:{tds:.0f}, pH:{ph:.2f}, Vib:{vibration:.3f}")

                # 🔹 ML PREDICTION
                sample = np.array([[flow, pressure, tds, vibration]])
                prediction = model.predict(sample)[0]

                command = None

                if prediction == -1:
                    print("🚨 Anomaly detected by ML")

                    # 🔍 RELATIVE FEATURE ANALYSIS (NO FIXED THRESHOLDS)

                    # Normalize using baseline mean
                    baseline_mean = np.mean(X, axis=0)
                    norm = sample / baseline_mean

                    flow_score = norm[0][0]
                    pressure_score = norm[0][1]
                    tds_score = norm[0][2]
                    vib_score = norm[0][3]

                    print(f"🔎 Scores → Flow:{flow_score:.2f}, TDS:{tds_score:.2f}, Vib:{vib_score:.2f}")

                    # Determine dominant anomaly cause
                    if tds_score > vib_score and tds_score > flow_score:
                        print("🧪 Likely contamination → SHUT VALVE")
                        command = "FULL"

                    elif vib_score > tds_score:
                        print("🔧 Likely pipe issue → SHUT VALVE")
                        command = "FULL"

                    else:
                        print("💧 Likely flow anomaly")

                        if flow_score < 0.5:
                            command = "HALF"
                            print("➡️ Opening valve (HALF)")
                        else:
                            command = "QUAT"
                            print("➡️ Adjusting valve (QUAT)")

                else:
                    print("✅ System normal → no change")
                    command = None

                # 🔥 SEND ONLY IF STATE CHANGES
                if command is not None and command != current_state:
                    ser.write((command + "\n").encode())
                    print(f"📡 Command Sent: {command}")
                    current_state = command

        except Exception as e:
            print("⚠️ Parse error:", line)

    time.sleep(0.1)  # prevent flooding
