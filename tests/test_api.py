from fastapi.testclient import TestClient

from app.adapters_fake import FakeRatesAdapter
from app.api import get_rates_port
from app.main import app


def override_rates():
    return FakeRatesAdapter({("USD", "PEN"): 3.0})


app.dependency_overrides[get_rates_port] = override_rates


client = TestClient(app)


def test_convert_endpoint_ok():
    """
    GIVEN   the FastAPI app with dependency override returning rate=3.0
    WHEN    calling GET /convert with amount=100, from_=USD, to=PEN
    THEN    the response status should be 200 and the JSON should include
            rate=3.0, converted=300.0, and source="fake"
    """
    r = client.get("/convert", params={"amount": 100, "from_": "USD", "to": "PEN"})
    assert r.status_code == 200
    data = r.json()
    assert data["rate"] == 3.0
    assert data["converted"] == 300.0
    assert data["source"] == "fake"


def test_convert_endpoint_validation():
    """
    GIVEN the FastAPI app with dependency override
    WHEN calling GET /convert with amount=0 (invalid by query validation)
    THEN the response status should be 422 (Unprocessable Entity)
    """
    r = client.get("/convert", params={"amount": 0, "from_": "USD", "to": "PEN"})
    assert r.status_code == 422
    data = r.json()
    assert data["detail"][0]["loc"][-1] == "amount"
