import pytest
from calculator import Calculator

# Addition Tests
def test_add_positive_numbers():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_add_negative_numbers():
    calc = Calculator()
    assert calc.add(-2, -3) == -5

def test_add_with_zero():
    calc = Calculator()
    assert calc.add(5, 0) == 5


# Subtraction Tests
def test_subtract_basic():
    calc = Calculator()
    assert calc.subtract(10, 3) == 7
    assert calc.subtract(0, 5) == -5


# Multiplication Tests 
def test_multiply_basic():
    calc = Calculator()
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(-3, 5) == -15


# --- Division Tests ---
def test_divide_basic():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(7, 2) == 3.5


def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(5, 0)
