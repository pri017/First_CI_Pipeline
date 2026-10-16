import importlib

largest_word = importlib.import_module("21_largest_word").largest_word


def test_simple():
    assert largest_word("I love programming") == "programming"


def test_punctuation():
    assert largest_word("Hello, world!") == "Hello"


def test_tie():
    assert largest_word("cat dog bat") == "cat"


def test_single():
    assert largest_word("Python") == "Python"


def test_empty():
    assert largest_word("") == ""


def test_only_punctuation():
    assert largest_word("!!! ...") == ""
