from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import RequestContract, ResponseContract
from services import calculate_ev
import sys
import logging

logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)
logger = logging.getLogger("fraud_engine")
logger.setLevel(logging.INFO)

MODEL_VERSION = "v1"
FEATURE_VERSION = "v1.0"

app = FastAPI()

@app.get("/health")
async def getHealth():
    return {"status": "ok",
            "model_version": MODEL_VERSION,
            "feature_version": FEATURE_VERSION}

@app.post("/v1/decide")
async def getRequestContract(request: RequestContract):
    response = calculate_ev(request)

    logger.info({
        "order_id": request.order_id,
        "item_value": request.item_value,
        "resale_value": request.resale_value,
        "return_history_count": request.return_history_count,
        "order_history_count": request.order_history_count,
        "e_ltv": request.e_ltv,
        "action": response.action,
        "expected_savings": response.expected_savings,
        "fraud_probability": response.fraud_probability,
    })

    return response