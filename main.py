from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import RequestContract, ResponseContract
from services import calculate_ev
import logging
logger = logging.getLogger("fraud_engine")

MODEL_VERSION = "v1"
FEATURE_VERSION = "v1.0"

app = FastAPI()

@app.get("/health")
async def getHealth():
    return {"status": "ok",
            "model_version": MODEL_VERSION,
            "feature_version": FEATURE_VERSION}

@app.post("/v1/decide")
async def getRequestContract(request_contract: RequestContract):

    if request_contract.item_value < 0:
        raise HTTPException(status_code=400, detail="invalid input")

    response = calculate_ev(request_contract)

    logger.info({
        "item_value": request_contract.item_value,
        "order_id": request_contract.order_id,
        "action": response.action,
        "fraud_probability": response.fraud_probability,
        "expected_savings": response.expected_savings
    })

    return response