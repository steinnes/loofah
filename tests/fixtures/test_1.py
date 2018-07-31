import pytest


@pytest.fixture
def fixture1():
    return None


def test_1(fixture1):
    (a, b, c, d) = (1, 2, 3, 4)
