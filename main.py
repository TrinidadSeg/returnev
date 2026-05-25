from fastapi import FastAPI
from pydantic import BaseModel

class RequestContract(BaseModel):
    item_value: float
    return_shipping_cost: float
    resale_value: float
    customer_return_rate: float
    order_history_count: int

class ResponseContract(BaseModel):
    action: str
    expected_savings: float
    confidence: float
    reasoning: str

app = FastAPI()

@app.get("/health")
async def getHealth():
    return {"status": "ok"}

@app.post("/v1/decide")
async def getRequestContract(request_contract: RequestContract):
    return ResponseContract(
        action = "keep_item",
        expected_savings = 8.50,
        confidence = 0.87,
        reasoning = "Hardcoded placeholder decision."
    )
