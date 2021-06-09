import pytest

def test_failprogram():
    msg = "hello"
    assert msg == "hi"


@pytest.mark.smoke
def test_passprogramtxt(firstprogram):
    msg = "hello"
    assert msg == "hello "
