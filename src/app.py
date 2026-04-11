from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="Retail Demand Forecasting API", version="2.0")

app.include_router(router)
