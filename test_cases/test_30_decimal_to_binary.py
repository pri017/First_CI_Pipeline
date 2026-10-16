import importlib
import pytest

decimal_to_binary = importlib.import_module("30_decimal_to_binary").decimal_to_binary


def test_normal():
    assert decimal_to_binary(10) == "1010"


def test_zero():
    assert decimal_to_binary(0) == "0"


def test_one():
    assert decimal_to_binary(1) == "1"


def test_power_of_two():
    assert decimal_to_binary(16) == "10000"


def test_odd():
    assert decimal_to_binary(31) == "11111"


def test_negative_error():
    with pytest.raises(ValueError):
        decimal_to_binary(-1)
