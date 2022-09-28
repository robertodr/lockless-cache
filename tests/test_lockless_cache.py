import pytest

from lockless_cache import __version__, sum_two_ints


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.parametrize(
    "expected,lhs,rhs",
    [
        (2, 3, -1),
        (4, 2, 2),
        (8, -10, 18),
        (8, 6, 2),
    ],
)
def test_sum_two_ints(expected, lhs, rhs):
    assert expected == sum_two_ints(lhs, rhs)
