import importlib
import pytest

find_max_min = importlib.import_module("25_max_min_list").find_max_min


def test_normal():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)


def test_single():
    assert find_max_min([5]) == (5, 5)


def test_negative():
    assert find_max_min([-4, -9, -1]) == (-1, -9)


def test_duplicates():
    assert find_max_min([2, 2, 2]) == (2, 2)


def test_empty_error():
    with pytest.raises(ValueError):
        find_max_min([])
