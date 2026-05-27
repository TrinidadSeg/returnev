from fastapi import FastAPI
from pydantic import BaseModel
from models import RequestContract, ResponseContract
from services import calculate_ev


app = FastAPI()

@app.get("/health")
async def getHealth():
    return {"status": "ok"}

@app.post("/v1/decide")
async def getRequestContract(request_contract: RequestContract):
    return calculate_ev(request_contract)
