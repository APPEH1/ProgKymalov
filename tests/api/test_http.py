import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(r.text)

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    print(f"Response Headers are {r.headers}")

#тест на статус код 404 (помилка)
@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')
    
    assert r.status_code == 404
    
