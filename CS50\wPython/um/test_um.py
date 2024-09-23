from um import count

def test_beg_end():
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album.") == 1
    assert count("um?") == 1
    assert count("Um, thanks, um..") == 2
    assert count("Um, thanks, um, I really appreciate it, um...") == 3
    assert count("UM") == 1

def test_characters():
    assert count("Um, thanks, that was yummy...") == 1
    assert count("What did you?Um?Say?") == 1
    assert count("YUMMY") == 0
    assert count("yumyum") == 0

def test_other():
    assert count("Um, I think its yummy, um, yumyum!") == 2
    assert count("Hello, um.") == 1