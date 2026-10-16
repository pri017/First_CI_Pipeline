import importlib

sum_of_list = importlib.import_module("26_sum_of_list").sum_of_list


def test_normal():
    assert sum_of_list([1, 2, 3, 4]) == 10


def test_empty():
    assert sum_of_list([]) == 0


def test_single():
    assert sum_of_list([8]) == 8


def test_negative():
    assert sum_of_list([-2, -3, 1]) == -4


def test_decimals():
    assert sum_of_list([1.5, 2.25]) == 3.75
