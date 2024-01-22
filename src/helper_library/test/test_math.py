from helper_library.math import add, subtract


def test_add():
    """Test the add function."""
    assert add(7, 3) == 10


def test_subtract():
    """Test the subtract function."""
    assert subtract(7, 3) == 4
