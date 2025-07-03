import pytest
from Calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_sub():
    calc = Calculator()
    assert calc.sub(5, 3) == 2
    assert calc.sub(0, 4) == -4

def test_mul():
    calc = Calculator()
    assert calc.mul(2, 3) == 6
    assert calc.mul(-2, 3) == -6

def test_div():
    calc = Calculator()
    assert calc.div(6, 3) == 2.0
    assert calc.div(7, 2) == 3.5

def test_div_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.div(5, 0)
