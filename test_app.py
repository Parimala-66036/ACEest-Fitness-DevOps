
import pytest
from app import app, init_db


@pytest.fixture
def client(tmp_path):
    app.config["TESTING"] = True
    app.config["DATABASE"] = str(tmp_path / "test_gym.db")

    with app.app_context():
        init_db()

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"ACEest Fitness & Gym" in response.data


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_register_member(client):
    response = client.post("/members", json={
        "name": "Rahul Kumar",
        "email": "rahul@example.com",
        "phone": "9876543210"
    })

    assert response.status_code == 201
    assert response.json["message"] == "Member registered successfully"


def test_get_members(client):
    client.post("/members", json={
        "name": "Rahul Kumar",
        "email": "rahul@example.com",
        "phone": "9876543210"
    })

    response = client.get("/members")

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["name"] == "Rahul Kumar"


def test_duplicate_email(client):
    member = {
        "name": "Rahul Kumar",
        "email": "rahul@example.com",
        "phone": "9876543210"
    }

    client.post("/members", json=member)
    response = client.post("/members", json=member)

    assert response.status_code == 409


def test_missing_member_details(client):
    response = client.post("/members", json={
        "name": "Rahul Kumar"
    })

    assert response.status_code == 400

def test_search_member_by_name(client):
    client.post("/members", json={
        "name": "Rahul Kumar",
        "email": "rahul@example.com",
        "phone": "9876543210"
    })

    response = client.get("/members?search=Rahul")

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["name"] == "Rahul Kumar"


def test_search_member_no_match(client):
    response = client.get("/members?search=Unknown")

    assert response.status_code == 200
    assert response.json == []
