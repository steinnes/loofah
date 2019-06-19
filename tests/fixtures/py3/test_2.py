import pytest
try:
    from unittest import mock
except ImportError:
    import mock



class FakeClass:
    pass


@pytest.fixture
def fixture2():
    return FakeClass()


def test_3(fixture2: FakeClass):
    (a, b, c, d) = (1, 2, 3, 4)
