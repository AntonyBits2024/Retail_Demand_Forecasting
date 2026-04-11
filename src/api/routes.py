from fastapi import APIRouter, HTTPException
from src.data.load_data import load_data
from src.features.feature_engineering import create_features
from src.models.train_model import train_model
from src.models.predict import predict
from src.utils.logger import logger

router = APIRouter()

@router.get("/")
def home():
    return {"message": "API Running"}

@router.post("/train")
def train():
    try:
        df = load_data()
        df = create_features(df)
        train_model(df)
        return {"status": "trained"}
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail="Training failed")

@router.post("/predict")
def get_prediction(data: dict):
    try:
        result = predict(data)
        return {"prediction": result}
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail="Prediction failed")
