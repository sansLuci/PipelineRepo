import Calculator
import pytest

def test_add():
	assert Calculator.add(2,3) == 5

def test_subtract():
	assert Calculator.subtract(2,3) == 1

def test_product():
	assert Calculator.product(2,3) == 6

def test_division():
	assert Calculator.division(2,3) == 0
