from calculator import add, multiply


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(0, 5) == 0
