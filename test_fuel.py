from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("3/4") == 75

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert(1/0, testing=True)
        
def test_value_error():
    with pytest.raises(ValueError):
        convert("4/2", testing=True)

def test_value_error_again():
    with pytest.raises(ValueError) as excinfo:
        convert("a/2", testing=True)
    assert "Invalid Fraction" in str(excinfo)