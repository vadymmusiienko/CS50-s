from working import convert
import pytest

def test_first_form():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("9:59 AM to 5:30 PM") == "09:59 to 17:30"
    assert convert("9:20 AM to 5:51 PM") == "09:20 to 17:51"

def test_second_form():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("9 PM to 5:23 AM") == "21:00 to 05:23"

def test_wrong():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9:60 AM to 9:00 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 9 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 13 AM")