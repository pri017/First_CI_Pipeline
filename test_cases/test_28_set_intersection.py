import importlib

set_intersection = importlib.import_module("28_set_intersection").set_intersection


def test_normal():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_empty():
    assert set_intersection(set(), {1}) == set()


def test_disjoint():
    assert set_intersection({1, 2}, {3, 4}) == set()


def test_equal():
    assert set_intersection({1, 2}, {1, 2}) == {1, 2}


def test_negative():
    assert set_intersection({-2, -1, 0}, {-1, 0, 3}) == {-1, 0}
