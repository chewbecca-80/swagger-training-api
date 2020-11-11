'''Functional Tests

These tests test a running instance of service to make sure it is functional
'''
import requests
import json

def test_health():
    response = requests.get('http://localhost:9090/v1/health')
    assert response.status_code == 200
    assert response.json() == {'message': 'Everything is A-OK'}

def test_echo():
    response = requests.get('http://localhost:9090/v1/echo/hello')
    assert response.status_code == 200
    assert response.json() == {'echo': 'hello hello hello'}
