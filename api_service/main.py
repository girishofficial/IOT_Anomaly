from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import numpy as np
import joblib
import os

# Load model
model = joblib.load('best_model_iso.pkl')

# Create FastAPI app
app = FastAPI()

# Set templates directory
templates = Jinja2Templates(directory="templates")

# Pydantic model for API input
class SensorData(BaseModel):
    vent: float
    pluie: float
    temp: float

# Predict API (same as before)
@app.post("/predict")
def predict(data: SensorData):
    features = np.array([[data.vent, data.pluie, data.temp]])
    prediction = model.predict(features)
    status = "anomaly" if prediction[0] == -1 else "normal"
    return {"status": status}

# Frontend: serve HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

