from twttr import shorten



def test_letters():
    assert shorten("twitter") == "twttr"
    assert shorten("CAT") == "CT"
    assert shorten("bcd") == "bcd"
    assert shorten("aeou") == ""

def test_num():
    assert shorten("123") == "123"
    assert shorten("1a2b3A") == "12b3"

def test_symblos():
    assert shorten("Hello, world") == "Hll, wrld"
    assert shorten("You&ME") == "Y&M"