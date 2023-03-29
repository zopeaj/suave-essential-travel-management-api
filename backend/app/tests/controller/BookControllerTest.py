import os
import sys
path = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi.testclient import TestClient
from app.test.db.SessionTest import app
from testtool import TestCase


class BookControllerTest:
    def __init__(self):
        self.client = TestClient(app)
        self.booking_id = None

    def test_create_booking():
        response = self.client.post("/booking/", json={"user": "used_id", "country": "nigeria", "state": "abuja", "hotel": "abuja-hotel"})
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["hotel"] == "abuja-hotel"
        assert "id" in data
        user_id = data["used_id"]
        self.booking_id = data["booking_id"]

    def test_get_booking_id():
        response = self.client.get(f"/booking/{booking_id}")
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["email"] == "user-email"
        assert data["id"] ==


    def test_update_booking():
        response = self.client.put(f"/booking/{booking_id}", json={"user": "used_id", "country": "croatia", "state": "", "hotel": "country-hotel"})
        assert response.status_code == 203, response.text
        data = response.json()
        assert data[""] == ""
        assert "id" in data


    def test_delete_booking():
        response = self.client.delete(f"/booking/{booking_id}")
        assert response.status_code == 304, response.text
        data = response.json()
        assert id not data


