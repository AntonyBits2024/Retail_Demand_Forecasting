import pandas as pd
from src.config.config import DATA_PATH
from src.utils.logger import logger

def load_data():
    try:
        logger.info("Loading dataset")
        df = pd.read_csv(DATA_PATH)
        df['date'] = pd.to_datetime(df['date'])
        return df
    except Exception as e:
        logger.error(str(e))
        raise
