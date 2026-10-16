import importlib

merge_sorted_lists = importlib.import_module("24_merge_sorted_lists").merge_sorted_lists


def test_normal():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_empty():
    assert merge_sorted_lists([], []) == []


def test_left_empty():
    assert merge_sorted_lists([], [1, 2]) == [1, 2]


def test_right_empty():
    assert merge_sorted_lists([1, 2], []) == [1, 2]


def test_negative_duplicates():
    assert merge_sorted_lists([-3, 1, 1], [-2, 1]) == [-3, -2, 1, 1, 1]


def test_inputs_unchanged():
    first, second = [1, 3], [2, 4]
    result = merge_sorted_lists(first, second)
    assert first == [1, 3]
    assert second == [2, 4]
    assert result is not first and result is not second
