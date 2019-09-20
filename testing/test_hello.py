import pytest
import requests

def test_hello():
    assert(1 == 1)

def test_webserver():
    r = requests.get('http://localhost:80')
    assert r.status_code == 200
    assert 'Hello World' in r.text
