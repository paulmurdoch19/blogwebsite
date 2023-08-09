import pytest

from blogwebsite.app import app



@pytest.fixture()
def client():
    return app.test_client()

# Test if the routes return expected responses
def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "<h1>Hello, World!</h1>" in response.text

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert "About Page" in response.text

def test_home(client):
    response = client.get('/home')
    assert response.status_code == 200
    assert "Home Page" in response.text

def test_test(client):
    response = client.get('/test')
    assert response.status_code == 200
    assert "this is a test route" in response.text
