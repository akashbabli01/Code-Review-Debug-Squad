import pytest
from divide_utils import divide

def test_normal_division():
    assert divide(10, 2) == 5

def test_float_division():
    assert divide(5.5, 2) == 2.75

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_invalid_input():
    with pytest.raises(TypeError):
        divide("10", 2)
