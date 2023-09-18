from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import pandas as pd
from challenge.model import DelayModel
import os
from typing import List

app = FastAPI()

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), '../data/data.csv')

model = DelayModel()
data_training = pd.read_csv(DATA_FILE_PATH)
features_model, target_model = model.preprocess(
    data=data_training,
    target_column="delay"
)
model.fit(
    features=features_model,
    target=target_model
)

class FlightInput(BaseModel):
    OPERA: str
    TIPOVUELO: str
    MES: int

class InputData(BaseModel):
    flights: List[FlightInput]

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {"status": "OK"}

def validate_flight(flight):
    if "MES" in flight and not (0 < flight["MES"] < 13):
        return False
    
    if "TIPOVUELO" in flight and flight["TIPOVUELO"].upper() not in ["I", "N"]:
        return False
    
    return True

@app.post("/predict", status_code=200)
async def post_predict(input_data: InputData) -> dict:
    validated_data = []
    for flight in input_data.flights:
        if not validate_flight(flight.dict()):
            raise HTTPException(status_code=400, detail="failed_unkown_column")
        validated_data.append(flight.dict())
    
    new_data = pd.DataFrame(validated_data)
    features = model.preprocess(new_data)
    predictions = model.predict(features)
    return {"predict": predictions.tolist()}
