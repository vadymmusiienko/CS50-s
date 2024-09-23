from seasons import get_date, get_minutes
import pytest
import datetime

def test_date():
    assert get_date("2005-05-13") == datetime.date(2005, 5, 13)

    with pytest.raises(SystemExit):
        get_date("2005-13-105")

    with pytest.raises(SystemExit):
        get_date("05/13/2005")

    with pytest.raises(SystemExit):
        get_date("13/05/2005")

    with pytest.raises(SystemExit):
        get_date("05-13-2005")

    with pytest.raises(SystemExit):
        get_date("13-05-2005")

    with pytest.raises(SystemExit):
        get_date("")

    with pytest.raises(SystemExit):
        get_date("13 Jan 2005")

    with pytest.raises(SystemExit):
        get_date("2025-13-")


def test_minutes():
    assert get_minutes(get_date("2005-05-13")) == "Nine million, seven hundred eighty thousand, four hundred eighty minutes"
