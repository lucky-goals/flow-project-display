from src.add import add, add_v9, add_v10, add_v11


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_zero():
    assert add(0, 5) == 5
    assert add(0, 0) == 0


def test_add_floats():
    assert add(1.5, 2.5) == 4.0


# --- add_v9 tests ---


def test_add_v9_positive_numbers():
    assert add_v9(2, 3) == 5


def test_add_v9_negative_numbers():
    assert add_v9(-1, -2) == -3


def test_add_v9_zero():
    assert add_v9(0, 5) == 5
    assert add_v9(0, 0) == 0


def test_add_v9_floats():
    assert add_v9(1.5, 2.5) == 4.0


# --- add_v10 tests ---


def test_add_v10_positive_numbers():
    assert add_v10(2, 3) == 5


def test_add_v10_negative_numbers():
    assert add_v10(-1, -2) == -3


def test_add_v10_zero():
    assert add_v10(0, 5) == 5
    assert add_v10(0, 0) == 0


def test_add_v10_floats():
    assert add_v10(1.5, 2.5) == 4.0


# --- add_v11 tests ---


def test_add_v11_positive_numbers():
    assert add_v11(2, 3) == 5


def test_add_v11_negative_numbers():
    assert add_v11(-1, -2) == -3


def test_add_v11_zero():
    assert add_v11(0, 5) == 5


def test_add_v11_floats():
    assert add_v11(1.5, 2.5) == 4.0


# --- add_v11 tests ---


def test_add_v11_positive_numbers():
    assert add_v11(2, 3) == 5


def test_add_v11_negative_numbers():
    assert add_v11(-1, -2) == -3


def test_add_v11_zero():
    assert add_v11(0, 5) == 5


def test_add_v11_floats():
    assert add_v11(1.5, 2.5) == 4.0
