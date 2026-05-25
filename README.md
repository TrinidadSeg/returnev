# ReturnEV

An API that helps online merchants decide what to do with a returned item — refund it, deny the return, or just let the customer keep it, and tells them how much each choice is expected to save.

## What it does

For each return request, ReturnEV weighs the tradeoffs" item value, return shipping cost, resale value, and the customer's return history and responds with a recommended **action**, the **expected savings** of that action, and a **confidence** score.

> **Status:** The API contract and pipeline are live. The decision currently returns a placeholder while the expected-value and fraud-risk models are in progress.

## Run it locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open **http://127.0.0.1:8000/docs** to explore the API and fire a live request right in your browser.

## Example

`POST /v1/decide`

Request:
```json
{
  "item_value": 45.00,
  "return_shipping_cost": 12.00,
  "resale_value": 20.00,
  "customer_return_rate": 0.6,
  "order_history_count": 3
}
```

Response:
```json
{
  "action": "keep_item",
  "expected_savings": 8.50,
  "confidence": 0.87,
  "reasoning": "Hardcoded placeholder decision."
}
```

## Endpoints

- `POST /v1/decide` — takes a return request and returns a recommended action with its expected savings and a confidence score.
- `GET /health` — liveness check; returns `{"status": "ok"}`.

## Tech

Built with Python and FastAPI. Request/response validation and the interactive docs page come from Pydantic and FastAPI's built-in OpenAPI support.