def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "Healthy"}


def test_non_existent_route(client):
    response = client.get("/non-existent-route-12345")
    assert response.status_code == 404


def test_docs_page_exists(client):
    response = client.get("/docs")
    assert response.status_code == 200


# def test_signup(client):
#     response = client.post(
#         "/auth/signup", json={"first_name": "Test", "last_name": "User", "email": "test@example.com", "password": "strongpassword123"}
#     )
#     assert response.status_code in [200, 201]


# def test_login(client):
#     response = client.post(
#         "/auth/login", json={"email": "test@example.com", "password": "strongpassword123"}
#     )
#     assert response.status_code == 200
