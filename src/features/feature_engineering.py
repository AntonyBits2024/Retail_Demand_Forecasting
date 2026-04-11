from src.utils.logger import logger

def create_features(df):
    try:
        df = df.sort_values("date")
        df["day_of_week"] = df["date"].dt.dayofweek
        df["month"] = df["date"].dt.month
        df["lag_1"] = df["sales"].shift(1)
        df["lag_7"] = df["sales"].shift(7)
        df["rolling_mean_7"] = df["sales"].rolling(7).mean()
        return df.dropna()
    except Exception as e:
        logger.error(str(e))
        raise
