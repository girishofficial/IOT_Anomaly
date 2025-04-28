from fastapi import FastAPI
import pandas as pd
import requests
import time

app = FastAPI()
THRESHOLD = 0.1

@app.get("/monitor")
def monitor_data():
    df = pd.read_csv('../data_collection_service/data_store.csv')
    if len(df) < 2:
        return {"status": "Not enough data"}
    
    change = abs(df.iloc[-1]['tmin'] - df.iloc[-2]['tmin']) / df.iloc[-2]['tmin']
    
    if change > THRESHOLD:
        requests.post("http://retraining_service:8000/retrain")  # microservice call
        return {"status": "Anomaly detected, retraining triggered"}
    return {"status": "No anomaly"}

