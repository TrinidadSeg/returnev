import math
from models import RequestContract

Betas = {
    "intercept": -3.2,
    "item_value": 0.001,
    "resale_value_ratio": 2.8,
    "return_rate": 3.5,
    "e_ltv": -0.0001
}

def calculate_fraud(request: RequestContract) -> float:
    # Logic to Calculate Fraud Probability
    z = (
        Betas["intercept"] +
        Betas["item_value"] * request.item_value + 
        Betas["resale_value_ratio"] * request.resale_value / max(request.item_value, 1) + 
        Betas["return_rate"] * request.return_history_count / max(request.order_history_count, 1) + 
        Betas["e_ltv"] * request.e_ltv
    )
    p_fraud = 1 / (1 + math.exp(-z))
    return p_fraud