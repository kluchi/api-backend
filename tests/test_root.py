from fastapi.testclient import TestClient
from pytest import fixture
from main import app


@fixture
def client():
    return TestClient(app)


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
