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
