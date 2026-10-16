import importlib

is_anagram = importlib.import_module("22_anagram_strings").is_anagram


def test_basic():
    assert is_anagram("listen", "silent") is True


def test_not_anagram():
    assert is_anagram("hello", "world") is False


def test_case_and_spaces():
    assert is_anagram("Dormitory", "Dirty room") is True


def test_empty():
    assert is_anagram("", " ") is True


def test_repeated_letters():
    assert is_anagram("aab", "abb") is False


def test_different_lengths():
    assert is_anagram("ab", "abc") is False
