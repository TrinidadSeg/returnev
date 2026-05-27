from models import RequestContract, ResponseContract
from .fraud_calculator import calculate_fraud

def calculate_ev(request: RequestContract) -> ResponseContract:
    p_fraud = calculate_fraud(request)
    return_resell_ev = (
        (request.p_next_order_return_fraud * p_fraud +
        request.p_next_order_return_not_fraud * (1 - p_fraud)) * request.e_ltv
        + request.resale_value
        - request.item_value
    )
    keep_it_ev = (
        (request.p_next_order_keep_fraud * p_fraud +
        request.p_next_order_keep_not_fraud * (1 - p_fraud)) * request.e_ltv
        - request.item_value
    )
    deny_it_ev = (
        (request.p_next_order_deny_fraud * p_fraud +
        request.p_next_order_deny_not_fraud * (1 - p_fraud)) * request.e_ltv
    )
    response = ResponseContract(
        action="calculate_ev",
        expected_savings=max(return_resell_ev, keep_it_ev, deny_it_ev),
        confidence=p_fraud,
        reasoning="Expected value calculated based on fraud probabilities."
    )
    if response.expected_savings == return_resell_ev:
        response.action = "return_and_resell"
    elif response.expected_savings == keep_it_ev:
        response.action = "keep_it"
    else:
        response.action = "deny_it"
    return response

