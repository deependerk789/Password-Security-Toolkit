import pytest
from app import app

@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    with app.test_client() as c:
        yield c

def test_home_page(client):
    r=client.get("/")
    assert r.status_code==200 and b"Sign in to SecureCheck" in r.data

def test_report_shows_details_and_maskable_password(client):
    r=client.post("/analyze",data={"name":"Demo User","email":"demo@example.com","password":"sample-only-password-83!"})
    assert r.status_code==200
    assert b"Analysis complete" in r.data
    assert b"Demo User" in r.data and b"demo@example.com" in r.data
    assert b"sample-only-password-83!" in r.data
    assert b"toggle-result-password" in r.data

def test_bad_form(client):
    assert client.post("/analyze",data={"name":"","email":"x@y.com","password":"sample"}).status_code==400

def test_health(client):
    assert client.get("/health").get_json()["status"]=="ok"
