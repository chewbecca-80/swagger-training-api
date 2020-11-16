from servaites.python_demo_api import echo


def test_make_echo():
    message = echo.make_echo("hello")
    test_message = "hello hello hello"
    assert test_message == message