import importlib

is_armstrong = importlib.import_module("29_armstrong_number").is_armstrong


def test_normal():
    assert is_armstrong(153) is True


def test_not_armstrong():
    assert is_armstrong(123) is False


def test_zero():
    assert is_armstrong(0) is True


def test_single():
    assert is_armstrong(7) is True


def test_negative():
    assert is_armstrong(-153) is False


def test_four_digits():
    assert is_armstrong(9474) is True
