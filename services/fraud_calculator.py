import math
from models import RequestContract

Betas = {
    "intercept": -4.5,
    "item_value": 0.001,
    "resale_value": 0.005,
    "return_history_count": 0.35,
    "order_history_count": -0.15,
    "e_ltv": -0.001
}

def calculate_fraud(request: RequestContract) -> float:
    # Logic to Calculate Fraud Probability
    z = (
        Betas["intercept"] +
        Betas["item_value"] * request.item_value + 
        Betas["resale_value"] * request.resale_value + 
        Betas["return_history_count"] * request.return_history_count + 
        Betas["order_history_count"] * request.order_history_count + 
        Betas["e_ltv"] * request.e_ltv
    )
    p_fraud = 1 / (1 + math.exp(-z))
    return p_fraud