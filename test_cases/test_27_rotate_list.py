import importlib

rotate_list = importlib.import_module("27_rotate_list").rotate_list


def test_normal():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_empty():
    assert rotate_list([], 3) == []


def test_single():
    assert rotate_list([7], 100) == [7]


def test_large():
    assert rotate_list([1, 2, 3], 5) == [2, 3, 1]


def test_negative():
    assert rotate_list([1, 2, 3, 4], -1) == [2, 3, 4, 1]


def test_zero():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]


def test_returns_copy_without_changing_input():
    original = [1, 2, 3]
    assert rotate_list(original, 1) == [3, 1, 2]
    result = rotate_list(original, 0)
    assert original == [1, 2, 3]
    assert result == original
    assert result is not original
