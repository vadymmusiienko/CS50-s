from fuel import gauge, convert
import pytest

def test_ValueError():
    with pytest.raises(ValueError):
        convert("ddd")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("3.0/2.0")


def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/3") == 33


def test_E():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_Z():
    assert gauge(50) == "50%"
    assert gauge(32) == "32%"