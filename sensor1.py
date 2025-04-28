import time
import random
import requests

API_URL = "http://192.168.49.2:32663/predict"  # Change accordingly

def generate_sensor_data():
    if random.random() < 0.95:  # 95% chance
        # Generate normal data
        vent = random.uniform(10, 30)       # normal wind speed
        pluie = random.uniform(0, 10)        # normal rainfall
        temp = random.uniform(15, 25)         # normal temperature
    else:
        # Generate anomaly data
        vent = random.uniform(70, 120)      # extremely high wind
        pluie = random.uniform(30, 80)      # heavy rain
        temp = random.uniform(-10, 50)       # very low or high temp
    
    return {
        "vent": vent,
        "pluie": pluie,
        "temp": temp
    }

while True:
    sensor_data = generate_sensor_data()
    try:
        response = requests.post(API_URL, json=sensor_data)
        print(f"Sent: {sensor_data} | Prediction: {response.json()}")
    except Exception as e:
        print(f"Error sending data: {e}")

    time.sleep(5)  # wait 5 seconds before sending next

