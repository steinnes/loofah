import pytest
import sys
from loofah import ListUnusedFixtures


def get_test(luf, name):
    for collected in luf.collected:
        fun, fixtures = collected
        if fun.name == name:
            return collected


def test_loofah():
    list_unused = ListUnusedFixtures()
    pytest_args = ['--collect-only', '-p', 'no:terminal', 'tests/fixtures']

    if sys.version_info > (3,):
        pytest_args.append('tests/fixtures/py3')

    pytest.main(pytest_args, plugins=[list_unused])
    f1 = get_test(list_unused, 'test_1')
    assert 'fixture1' in f1[1]

    f2 = get_test(list_unused, 'test_2')
    assert 'fixture1' in f2[1]

    if sys.version_info > (3,):
        f3 = get_test(list_unused, 'test_3')
        assert 'fixture2' in f3[1]
