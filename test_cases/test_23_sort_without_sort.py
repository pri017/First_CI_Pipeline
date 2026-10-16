import importlib

bubble_sort = importlib.import_module("23_sort_without_sort").bubble_sort


def test_normal():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_empty():
    assert bubble_sort([]) == []


def test_single():
    assert bubble_sort([7]) == [7]


def test_negative_and_duplicate():
    assert bubble_sort([3, -1, 3, 0, -5]) == [-5, -1, 0, 3, 3]


def test_already_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_original_list_unchanged_and_new_list_returned():
    original = [3, 1, 2]
    result = bubble_sort(original)
    assert original == [3, 1, 2]
    assert result == [1, 2, 3]
    assert result is not original
