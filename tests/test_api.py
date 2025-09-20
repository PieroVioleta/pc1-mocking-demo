from fastapi.testclient import TestClient

from app.adapters_fake import FakeRatesAdapter
from app.api import get_rates_port
from app.main import app


def override_rates():
    return FakeRatesAdapter({("USD", "PEN"): 3.0})


app.dependency_overrides[get_rates_port] = override_rates


client = TestClient(app)


def test_convert_endpoint_ok():
    r = client.get("/convert", params={"amount": 100, "from_": "USD", "to": "PEN"})
    assert r.status_code == 200
    data = r.json()
    assert data["rate"] == 3.0
    assert data["converted"] == 300.0
    assert data["source"] == "fake"


def test_convert_endpoint_validation():
    r = client.get("/convert", params={"amount": 0, "from_": "USD", "to": "PEN"})
    assert r.status_code == 400
