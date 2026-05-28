from pydantic import BaseModel, Field

class RequestContract(BaseModel):
    order_id: str
    item_value: float = Field(gt = 0)
    resale_value: float = Field(ge = 0)
    return_history_count: int = Field(ge = 0)
    order_history_count: int = Field(gt = 0)
    e_ltv: float = Field(gt = 0)
    p_next_order_return_fraud: float = 0 # Usually 0 since fraudalent behavior has no interest in product
    p_next_order_return_not_fraud: float = 0.4 # Based on Long-Time Data
    p_next_order_keep_fraud: float = 0 # Usually 0 since fraudalent behavior has no interest in product
    p_next_order_keep_not_fraud: float = 0.5 # Based on Long-Time Data
    p_next_order_deny_fraud: float = 0
    p_next_order_deny_not_fraud: float = 0.1 # Based on Long-Time Data

class ResponseContract(BaseModel):
    order_id: str
    action: str
    expected_savings: float
    fraud_probability: float
    reasoning: str