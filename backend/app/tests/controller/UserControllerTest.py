from fastapi.testclient import TestClient
from app.main import app
from testtool import TestCase


class UserControllerTest(TestCase):
    def __init__(self):
        self.client = TestCliet(app)

    app.on_event("startup")
    async def startup_event():
        user["123"] = {"id": "123", "email": "email@example.com"}
        user["121"] = {"id": "125", "email": "data@example.com"}

    def test_read_user():
        response = self.client.get("/user/234", headers={"X-Token": jwtConfig.get_fake_secret_token()})
        assert response.status_code == 200
        assert response.json() == {"email": "admin@example.com", "admin"}

    def test_read_user_bad_token():
        response = self.client.get("/user/234", headers={"X-Token":"hailhydra"})
        assert response.status_code == 400
        assert response.json() == {"detail": "Invalid X-Token header"}

    def test_read_inexistent_user():
        response = client.get("/user/12", headers={"X-Token": jwtConfig.get_fake_secret_token()})
        assert response.status_code == 404
        assert response.json() == {"detail": "User not found"}

    def test_create_user():
        response = self.client.post("/user/", headers={"X-Token": jwtConfig.get_fake_secret_token()}, json={"id": "1234", "email": "example@example.com"})
        assert response.status_code == 200
        assert response.json() == {"id": "1234", "email": "example@example.com"}

    def test_create_bad_token():
        response = self.client.post("/user/", headers={"X-Token":"hailhydra"}, json={"id": "1234", "email": "admin@example.com"},)

    def test_create_existing_user():
        response = self.client.post("/user/", headers={"X-Token":jwtConfig.get_fake_secret_token()}, json={"id":"123", "email":"example@example.com",},)
        assert response.status_code == 400
        assert response.json() == {"detail": "User already exists"}

    def test_override_in_users():
        response = self.client.get("/user/")
        assert response.status_code == 200
        assert response.json() == {}

    def test_override_in_items_with_q():
        response = self.client.get("/user/?q=foo")
        assert response.status_code == 200
        assert response.json() == {}

    def test_override_in_users_with_params():
        response = self.client.get("/user/?q=foo&skip=100&limit=200")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello Users!", "params": {"q": "foo", "skip": 5, "limit": 10}}
