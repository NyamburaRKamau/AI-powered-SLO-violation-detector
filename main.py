from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# Load model and scaler
model = joblib.load("slo_violation_model.pkl")
scaler = joblib.load("scaler.pkl")

app = FastAPI()

# Define input schema
class SLOInput(BaseModel):
    cpu_usage: float
    memory_usage: float
    request_latency: float
    error_rate: float
    disk_io: float

@app.post("/predict")
def predict(data: SLOInput):
    # Convert input to array and scale
    input_data = np.array([[data.cpu_usage, data.memory_usage, data.request_latency, data.error_rate, data.disk_io]])
    input_scaled = scaler.transform(input_data)
    
    # Predict
    prediction = model.predict(input_scaled)[0]
    
    return {"slo_violation": int(prediction)}