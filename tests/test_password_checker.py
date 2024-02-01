import pytest
from lib.password_checker import *

def test_password_checker():
    checker = PasswordChecker()
    assert checker.check("12345678") == True
    assert checker.check("1234567") == False
    assert checker.check("123456789") == True

def test_password_checker():
    checker = PasswordChecker()
    with pytest.raises(Exception):
        checker.check("1234567")
