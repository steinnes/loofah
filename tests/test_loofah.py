import pytest
from loofah import ListUnusedFixtures


def get_test(luf, name):
    for collected in luf.collected:
        fun, fixtures = collected
        if fun.name == name:
            return collected


def test_loofah():
    list_unused = ListUnusedFixtures()
    pytest.main(['--collect-only', '-p', 'no:terminal', 'tests/fixtures/'], plugins=[list_unused])
    f = get_test(list_unused, 'test_1')
    assert 'fixture1' in f[1]
