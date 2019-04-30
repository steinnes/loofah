import pytest
try:
    from unittest import mock
except ImportError:
    import mock


@pytest.fixture
def fixture1():
    return None


def test_1(fixture1):
    (a, b, c, d) = (1, 2, 3, 4)


@mock.patch('sys.stdout.write')
def test_2(mock_write, fixture1):
    a = 1
