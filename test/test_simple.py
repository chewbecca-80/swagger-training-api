import json

from servaites.python_demo_api import echo


def test_make_echo():
    message = echo.make_echo("hello")
    data = json.load({'message': 'hello hello hello'})
    assert data = message