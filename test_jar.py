from jar import Jar
import pytest
import logging

def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(4)
    assert jar.size == 8
    jar.deposit(4)
    assert jar.size == 12

def test_withdraw():
    ...

def test_full_jar_exception():
    with pytest.raises(ValueError, match="Jar is already full") as e:
        jar = Jar()
        jar.deposit(12)
        jar.deposit(1)
    assert str(e.value) == "Jar is already full"

def test_too_many_cookies_exception():
    with pytest.raises(ValueError, match="Too many cookies"):
        jar = Jar()
        jar.deposit(13)

def test_negativ_cookie_exception():
    with pytest.raises(ValueError, match="Negativ amount of cookies is impossible"):
        jar = Jar()
        jar.deposit(-1)    

def test_not_enough_exception():
    with pytest.raises(ValueError, match="Not enough cookies") as e:
        jar = Jar()
        jar.deposit(12)
        jar.withdraw(11)
        jar.withdraw(2)