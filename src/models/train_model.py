from xgboost import XGBRegressor
from src.config.config import FEATURE_COLUMNS, TARGET_COLUMN, MODEL_PATH
import joblib
from src.utils.logger import logger

def train_model(df):
    try:
        X = df[FEATURE_COLUMNS]
        y = df[TARGET_COLUMN]
        model = XGBRegressor(n_estimators=100, max_depth=5)
        model.fit(X, y)
        joblib.dump(model, MODEL_PATH)
        return model
    except Exception as e:
        logger.error(str(e))
        raise
