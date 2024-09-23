from numb3rs import validate

def test_num():
    assert validate("0.0.0.0") == True
    assert validate("12.153.198.0") == True
    assert validate("255.255.255.255") == True
    assert validate("255.0.255.0") == True
    assert validate("255.255.255.205") == True
    assert validate("-1.213.24.0") == False
    assert validate("256.12.43.5") == False
    assert validate("1000.34.124.4") == False
    assert validate("10.10.10.10.10") == False
    assert validate("10.10.10.270") == False


def test_other():
    assert validate("cat") == False
    assert validate("12.32.56,32") == False
    assert validate("Ip is 12.12.12.12") == False
    assert validate("0.0.0.0 is my IP") == False
    assert validate("") == False
