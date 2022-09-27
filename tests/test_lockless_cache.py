from lockless_cache import __version__, sum_two_ints


def test_version():
    assert __version__ == "0.1.0"


def test_foo():
    assert 3 == (1 + 2)


def test_bar():
    assert 2 == (1 + 1)


def test_sum_two_ints():
    assert 2 == sum_two_ints(3, -1)
