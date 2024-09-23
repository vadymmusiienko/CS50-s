from bank import value

def test_hello():
    assert value("heLLo") == 0
    assert value("hello, newman") == 0
    assert value(" HELLO THERE ") == 0

def test_h():
    assert value(" How You Doing?") == 20
    assert value("HOW ARE YOU?") == 20
    assert value(" how are you doing? ") == 20
    assert value("How ya doin?") == 20

def test_else():
    assert value("Whats up") == 100
    assert value("Yo!") == 100
    assert value("What's good?") == 100