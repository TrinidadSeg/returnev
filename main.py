from fastapi import FastAPI
from pydantic import BaseModel
from models import RequestContract, ResponseContract


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
