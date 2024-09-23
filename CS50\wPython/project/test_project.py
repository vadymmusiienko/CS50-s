from project import typos_count, get_time_limit, check_time_limit


def test_typos_count():
    assert typos_count(["hello", "world"], ["hello", "world"]) == 0
    assert typos_count(["helo", "world"], ["hello", "world"]) == 1
    assert typos_count(["hello", "world", "extra"], ["hello", "world"]) == 1
    assert typos_count(["hello"], ["hello", "world"]) == 1
    assert typos_count(["helo", "wrld"], ["hello", "world"]) == 2
    assert typos_count([""], ["hello", "world"]) == 2


def test_get_time_limit():
    assert get_time_limit("easy") == 30.0
    assert get_time_limit("medium") == 60.0
    assert get_time_limit("hard") == 120.0


def test_check_time_limit():
    start_time = 1000000
    limit = 60
    current_time = 1000030
    assert not check_time_limit(start_time, limit, current_time)

    start_time = 1000000
    limit = 60
    current_time = 1000061
    assert check_time_limit(start_time, limit, current_time)
