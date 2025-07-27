import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_book_class():
    response = client.post("/book", json={
        "class_id": 2,  # Zumba (assumed to exist)
        "client_name": "John Tester",
        "client_email": "john@example.com"
    })
    # Accept both success and "no slots" error
    assert response.status_code in (200, 400)

def test_get_bookings():
    response = client.get("/bookings", params={"email": "john@example.com"})
    # Accept both success and "no bookings found"
    assert response.status_code in (200, 404)
