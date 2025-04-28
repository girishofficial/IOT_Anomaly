import time
import random
import requests

API_URL = "http://192.168.49.2:32663/predict"  # Change port if needed

def generate_sensor_data():
    vent = random.uniform(0, 80)      # wind speed
    pluie = random.uniform(0, 20)     # rainfall mm
    temp = random.uniform(5, 40)       # temp in Celsius
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

