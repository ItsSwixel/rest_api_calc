import pytest
from calc_package import calc_module

def test_addition():
    assert calc_module.addition(10, 15) == 25, "You have an issue in addition function"
    assert calc_module.addition(1, 2) == 3, "You have an issue in addition function"
    assert calc_module.addition(15, 15) == 30, "You have an issue in addition function"
    assert calc_module.addition(-12, -11) == -23, "You have an issue in addition function"
    assert calc_module.addition(12, 0) == 12, "You have an issue in addition function"
    assert calc_module.addition(5.5, 4) == 9.5, "You have an issue in addition function"

def test_subtraction():
    assert calc_module.subtraction(10, 15) == -5, "You have an issue in sub function"
    assert calc_module.subtraction(10, 5) == 5, "You have an issue in sub function"
    assert calc_module.subtraction(15, 15) == 0, "You have an issue in sub function"
    assert calc_module.subtraction(5.5, 3) == 2.5, "You have an issue in sub function"

def test_division():
    assert calc_module.division(10, 2) == 5, "You have an issue in division function"
    assert calc_module.division(1, 2) == 0.5, "You have an issue in division function"
    assert calc_module.division(10, -5) == -2, "You have an issue in division function"
    assert calc_module.division(-10, -5) == 2, "You have an issue in division function"
    assert calc_module.division(15, 0) == "Division by zero exception", "You have an issue in division function"
    assert calc_module.division(0, 15) == "Division by zero exception", "You have an issue in division function"
    assert calc_module.division(5.5, 2) == 2.75, "You have an issue in division function"

def test_multiplication():
    assert calc_module.multiplication(10, 2) == 20, "You have an issue in multiplication function"
    assert calc_module.multiplication(10, 0) == 0, "You have an issue in multiplication function"
    assert calc_module.multiplication(0, 10) == 0, "You have an issue in multiplication function"
    assert calc_module.multiplication(10, -5) == -50, "You have an issue in multiplication function"
    assert calc_module.multiplication(-10, -5) == 50, "You have an issue in multiplication function"
    assert calc_module.multiplication(5.5, 2) == 11, "You have an issue in multiplication function"
