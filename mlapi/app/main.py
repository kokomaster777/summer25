from fastapi import FastAPI, HTTPException
from app.schemas import HealthData, PredictionResult
from app.predictor import predict_smoker

app = FastAPI(title="Smoking Prediction API")

@app.post("/predict", response_model=PredictionResult)
async def predict(data: HealthData):
    try:
        return {"smokes": predict_smoker(data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"message": "API для предсказания курения"}