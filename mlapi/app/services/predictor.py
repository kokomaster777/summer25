from fastapi import Depends
from app.ml.model import load_model
from app.ml.preprocessing import prepare_features

model = load_model()

async def get_prediction(data):
    features = prepare_features(data.dict())
    prediction = model.predict(features)
    return bool(prediction[0])