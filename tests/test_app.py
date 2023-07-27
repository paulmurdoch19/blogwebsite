import pytest
import requests

from blogwebsite.app import app



@pytest.fixture(scope='module')
def start_app():
    app.run(port=5000)

# Test if the routes return expected responses
def test_hello_world(start_app):
    response = requests.get('http://127.0.0.1:5000/')
    assert response.status_code == 200
    assert "<h1>Hello, World!</h1>" in response.text

def test_about(start_app):
    response = requests.get('http://127.0.0.1:5000/about')
    assert response.status_code == 200
    assert "About Page" in response.text

def test_home(start_app):
    response = requests.get('http://127.0.0.1:5000/home')
    assert response.status_code == 200
    assert "Home Page" in response.text

def test_test(start_app):
    response = requests.get('http://127.0.0.1:5000/test')
    assert response.status_code == 200
    assert "this is a test route" in response.text
