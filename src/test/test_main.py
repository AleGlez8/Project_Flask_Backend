import pytest
from datetime import datetime

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_user(client):
    response = client.post('/api/users', json={"username": "test_user", "email": "test@example.com", "password": "pass123"})
    assert response.status_code == 201

def test_create_restaurant(client):
    response = client.post('/api/restaurants', json={"name": "El Buen Sabor", "location": "Centro", "max_capacity": 50})
    assert response.status_code == 201

def test_create_reservation(client):
    reservation_date = datetime.now().strftime("%Y-%m-%d")
    client.post('/api/users', json={"username": "john", "email": "john@example.com", "password": "pass123"})
    client.post('/api/restaurants', json={"name": "El Buen Sabor", "location": "Centro", "max_capacity": 50})
    response = client.post('/api/reservations', json={
        "user_id": 1, "restaurant_id": 1, "reservation_date": reservation_date, "guests": 2
    })
    assert response.status_code == 201
