import joblib, pandas as pd
from src.config.config import MODEL_PATH
from src.utils.logger import logger

def predict(input_data):
    try:
        model = joblib.load(MODEL_PATH)
        df = pd.DataFrame([input_data])
        pred = model.predict(df)
        return float(pred[0])
    except Exception as e:
        logger.error(str(e))
        raise
