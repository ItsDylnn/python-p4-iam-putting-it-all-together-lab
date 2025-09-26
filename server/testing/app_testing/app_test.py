import pytest
from server.models import db, User

# The database will be cleaned automatically thanks to conftest.py

def test_creates_users_at_signup(client, app):
    """Test that a valid signup creates a user."""
    data = {"username": "testuser", "password": "password123"}
    response = client.post("/signup", json=data)
    
    assert response.status_code == 201

    with app.app_context():
        user = User.query.filter_by(username="testuser").first()
        assert user is not None
        assert user.username == "testuser"


def test_422s_invalid_users_at_signup(client, app):
    """Test that missing or invalid data returns a 422."""
    # Missing username
    data = {"password": "password123"}
    response = client.post("/signup", json=data)
    assert response.status_code == 422

    # Missing password
    data = {"username": "anotheruser"}
    response = client.post("/signup", json=data)
    assert response.status_code == 422
