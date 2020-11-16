'''Functional Tests

These tests test a running instance of service to make sure it is functional
'''
import requests
import json

URL = 'http://localhost:9090/v1/health'

def wait_for_api():
    code = 0
    count = 0
    while code != 200 and count < 100: 
        response = requests.get(URL)
        code = response.status_code
        print(f"{count} : {code}")
        if code != 200:
            count = count + 1
            sleep(2)
    sys.exit(0)

def test_health():
    wait_for_api()
    response = requests.get('http://localhost:9090/v1/health')
    assert response.status_code == 200
    assert response.json() == {'message': 'Everything is A-OK'}

def test_echo():
    wait_for_api()
    response = requests.get('http://localhost:9090/v1/echo/hello')
    assert response.status_code == 200
    assert response.json() == {'echo': 'hello hello hello'}
