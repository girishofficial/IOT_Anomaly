from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.post("/collect")
def collect_data(sensor_data: dict):
    df = pd.DataFrame([sensor_data])
    df.to_csv("data_store.csv", mode='a', header=not pd.io.common.file_exists('data_store.csv'), index=False)
    return {"message": "Data collected"}

