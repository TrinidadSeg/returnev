from models import RequestContract, ResponseContract
from .fraud_calculator import calculate_fraud

def calculate_ev(request: RequestContract) -> ResponseContract:
    # V1 Assumes Refund Amount is equal to item value and shipping is paid for by the customer
    p_fraud = calculate_fraud(request)
    return_resell_ev = (
        (request.p_next_order_return_fraud * p_fraud +
        request.p_next_order_return_not_fraud * (1 - p_fraud)) * request.e_ltv
        + request.resale_value - request.item_value
    )
    keep_it_ev = (
        (request.p_next_order_keep_fraud * p_fraud +
        request.p_next_order_keep_not_fraud * (1 - p_fraud)) * request.e_ltv - request.item_value
    )
    deny_it_ev = (
        (request.p_next_order_deny_fraud * p_fraud +
        request.p_next_order_deny_not_fraud * (1 - p_fraud)) * request.e_ltv
    )
    options  = {
        "Return and resell": return_resell_ev,
        "Keep it": keep_it_ev,
        "Deny it": deny_it_ev
    }
    best_action = max(options, key = options.get)
    response = ResponseContract(
        action = best_action,
        expected_savings = options[best_action],
        fraud_probability = p_fraud,
        reasoning = f"return and resell ${return_resell_ev:.2f}, keep ${keep_it_ev:.2f}, and deny ${deny_it_ev:.2f}, fraud_p={p_fraud:.2f}"
    )
    return response

