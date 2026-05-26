from models import RequestContract, ResponseContract

def calculate_ev(request: RequestContract) -> ResponseContract:
    if (request.resale_value < request.return_shipping_cost):
        if (request.customer_return_rate < 0.2 and request.order_history_count > 3): 
            action = "Refund no return"
            expected_savings = 0
        else:
            action = "Refund customer pays return"
            expected_savings = request.resale_value
    else:
        if (request.customer_return_rate < 0.2 and request.order_history_count > 3):
            action = "Refund business pays return"
            expected_savings = request.resale_value - request.return_shipping_cost
        else:
            action = "Refund customer pays return"
            expected_savings = request.resale_value

    

"""class RequestContract(BaseModel):
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
"""