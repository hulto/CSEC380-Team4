import pytest
import requests

url = 'http://localhost:9000/login'


def test_valid_login():
    payload = {
        'username': 'oneeyedgrape',
        'password': 'password123'
    }

    with requests.Session() as s:
        p = s.post(url, data=payload)
        assert p.status_code == 200
        assert p.url != url


def test_invalid_uname():
    payload = {
        'username': 'twoeyedgrape',
        'password': 'password123'
    }

    with requests.Session() as s:
        p = s.post(url, data=payload)
        assert p.status_code == 200
        assert p.url == url


def test_invalid_password():
    payload = {
        'username': 'oneeyedgrape',
        'password': 'password1234'
    }

    with requests.Session() as s:
        p = s.post(url, data=payload)
        assert p.status_code == 200
        assert p.url == url
