def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "Healthy"}


def test_signup(client):
    response = client.post(
        "/signup", json={"email": "test@example.com", "password": "strongpassword123"}
    )
    assert response.status_code in [200, 201]


def test_login(client):
    response = client.post(
        "/login", json={"email": "test@example.com", "password": "strongpassword123"}
    )
    assert response.status_code == 200
