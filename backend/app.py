from fastapi import FastAPI
from dhis2_client import fetch_data
from processing import process_data
from prediction import forecast_cases

app = FastAPI()

@app.get("/data")
def get_data():
    raw = fetch_data()
    df = process_data(raw)
    return df.to_dict()

@app.get("/forecast")
def get_forecast():
    raw = fetch_data()
    df = process_data(raw)
    forecast = forecast_cases(df)
    return forecast.to_dict()
