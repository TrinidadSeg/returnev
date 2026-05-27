from pydantic import BaseModel

class RequestContract(BaseModel):
    item_value: float
    resale_value: float
    return_history_count: float
    order_history_count: int
    e_ltv: float
    p_next_order_return_fraud: float = 0 # Usually 0 since fraudalent behavior has no interest in product
    p_next_order_return_not_fraud: float = 0.4 # Based on Long-Time Data
    p_next_order_keep_fraud: float = 0 # Usually 0 since fraudalent behavior has no interest in product
    p_next_order_keep_not_fraud: float = 0.5 # Based on Long-Time Data
    p_next_order_deny_fraud: float = 0
    p_next_order_deny_not_fraud: float = 0.1 # Based on Long-Time Data

class ResponseContract(BaseModel):
    action: str
    expected_savings: float
    confidence: float
    reasoning: str