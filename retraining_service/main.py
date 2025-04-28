from fastapi import FastAPI
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

app = FastAPI()

@app.post("/retrain")
def retrain_model():
    df = pd.read_csv('../data_collection_service/data_store.csv')
    X = df[['tmin', 'tmax', 'vent', 'pluie']]
    y = df['target']  # assuming target column exists
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, '../api_service/model.pkl')
    return {"message": "Model retrained and saved"}

