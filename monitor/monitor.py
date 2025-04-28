import requests
import time
import random
import subprocess

# Config
SENSOR_API_URL = "http://192.168.49.2:32663/predict"  # Adjust IP:Port
THRESHOLD = 10.0  # 10% anomaly
CHECK_INTERVAL = 10  # Check every 10 seconds
MINIMUM_SAMPLES = 20  # Must collect 20 samples before checking

# Statistics
total_count = 0
anomaly_count = 0

def generate_sensor_data():
    """Simulate realistic sensor data (normal + sometimes anomaly)."""
    if random.random() < 0.95:
        # Normal data 95% of time
        vent = random.uniform(10, 30)
        pluie = random.uniform(0, 10)
        temp = random.uniform(15, 25)
    else:
        # Anomaly data 5% of time
        vent = random.uniform(70, 120)
        pluie = random.uniform(30, 80)
        temp = random.uniform(-10, 50)
    return {
        "vent": vent,
        "pluie": pluie,
        "temp": temp
    }

while True:
    try:
        sensor_data = generate_sensor_data()
        response = requests.post(SENSOR_API_URL, json=sensor_data)
        prediction = response.json()["status"]

        total_count += 1
        if prediction == "anomaly":
            anomaly_count += 1

        # Print current stats
        print(f"Sent: {sensor_data} | Prediction: {prediction}")
        print(f"Total: {total_count} | Anomalies: {anomaly_count} | Anomaly Rate: {anomaly_count/total_count*100:.2f}%")

        if total_count >= MINIMUM_SAMPLES:
            anomaly_rate = (anomaly_count / total_count) * 100
            if anomaly_rate > THRESHOLD:
                print("🚨 High anomaly rate detected! Triggering retraining...")
                subprocess.call(["python3", "../retrain.py"])  # adjust if needed
                # Reset after retraining
                total_count = 0
                anomaly_count = 0

        time.sleep(CHECK_INTERVAL)

    except Exception as e:
        print(f"Error in monitoring: {e}")
        time.sleep(5)

