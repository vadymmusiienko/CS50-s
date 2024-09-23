from jar import Jar
import pytest

def test_init():
    jar = Jar(15)
    assert jar.capacity == 15
    jar = Jar()
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        jar = Jar(-19)
    with pytest.raises(ValueError):
        jar = Jar("12")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(20)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(15)
    assert jar.size == 20
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(10)
    assert jar.size == 0
    jar.deposit(8)
    jar.withdraw(3)
    assert jar.size == 5
    jar.withdraw(5)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
