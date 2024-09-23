from plates import is_valid

def test_len():
    assert is_valid("AAA1234") == False
    assert is_valid("A") == False

def test_start():
    assert is_valid("1AAA") == False
    assert is_valid("A123") == False
    assert is_valid("12AAA") == False

def test_num():
    assert is_valid("AA123A") == False
    assert is_valid("AA12AA") == False


def test_zero():
    assert is_valid("AAD01") == False
    assert is_valid("AA0123") == False


def test_symb():
    assert is_valid("AA,12") == False
    assert is_valid("AA!12") == False
    assert is_valid("AA 123") == False

def test_true():
    assert is_valid("AAA222") == True
    assert is_valid("AS42") == True
    assert is_valid("YES") == True