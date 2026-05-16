import pytest

from src.add import add


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0


def test_add_floats():
    assert add(1.5, 2.5) == 4.0
    assert add(-1.1, 1.1) == pytest.approx(0.0)
    assert add(0.1, 0.2) == pytest.approx(0.3)
