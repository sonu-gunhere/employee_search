from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_search_basic():
    response = client.get("/search/?org_id=org1&query=John")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any("name" in emp for emp in data)


def test_search_with_filters():
    response = client.get(
        "/search/?org_id=org1&query=&status=Active&department=HR&position=Manager"
    )
    assert response.status_code == 200
    data = response.json()
    for emp in data:
        assert emp.get("department") == "HR"
        assert emp.get("position") == "Manager"


def test_search_invalid_org():
    response = client.get("/search/?org_id=invalid&query=John")
    assert response.status_code == 200
    assert response.json() == []


def test_search_rate_limiting():
    for _ in range(10):
        client.get("/search/?org_id=org1&query=John")
    response = client.get("/search/?org_id=org1&query=John")
    assert response.status_code == 429
    assert response.json()["detail"] == "Rate limit exceeded"


def test_rate_limiting_hits_limit():
    org_id = "org1"
    url = f"/search/?org_id={org_id}&query=test"

    for i in range(11):
        response = client.get(url)

    assert response.status_code == 429
