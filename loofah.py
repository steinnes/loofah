# -*- coding: utf-8 -*-
import ast
import click
import inspect
import pytest


def unindent(code_lines):
    first_char_idx = 0
    for char in code_lines[0]:
        if char.isspace():
            first_char_idx += 1
        else:
            break

    unindented_block = []
    for line in code_lines:
        unindented_block.append(line[first_char_idx:])
    return unindented_block


def get_innermost_func(func):
    if '__wrapped__' in func.__dict__:
        return get_innermost_func(func.__dict__['__wrapped__'])
    return func


class TestFunction(object):
    def __init__(self, test):
        self.test = test
        self.func = get_innermost_func(test._getobj())
        self.code = self._get_code(self.func)
        self.loaded_fixtures = self.test.fixturenames
        self.declared_fixtures = self._get_declared_fixtures()
        self.used_locals = self._get_used_locals()

    def _get_code(self, func):
        function_definition = inspect.getsourcelines(func)
        return "".join(unindent(function_definition[0]))

    def _get_declared_fixtures(self):
        argspec = inspect.getargspec(self.func)
        ret = []
        for fixture in self.loaded_fixtures:
            if fixture in argspec.args:
                ret.append(fixture)
        return ret

    def _get_used_locals(self):
        root = ast.parse(self.code)
        function_body = root.body[0].body
        names = set()
        for node in function_body:
            node_names = set([n.id for n in ast.walk(node) if isinstance(n, ast.Name)])
            names.update(node_names)
        return names


class ListUnusedFixtures(object):
    def __init__(self, ignore=None):
        if ignore is None:
            ignore = []
        self.ignored_fixtures = ignore
        self.collected = []

    def list_unused_fixtures(self, test):
        func = TestFunction(test)
        missing = []
        for fixture in func.declared_fixtures:
            if fixture in self.ignored_fixtures:
                continue
            if fixture not in func.used_locals:
                missing.append(fixture)
        return missing

    def pytest_collection_modifyitems(self, items):
        for item in items:
            if not item.fixturenames:
                continue
            self.collected.append([item, self.list_unused_fixtures(item)])


def repr_function(func, unused_fixtures):
    filename, lineno, testname = func.location
    return u'{testpath} in {testname} detected {n_fixtures} unused fixture{plur}:\n{fixtures}'.format(
        plur='s' if len(unused_fixtures) % 10 != 1 else '',
        n_fixtures=click.style(str(len(unused_fixtures)), fg='red', bold=True),
        testname=click.style(testname, fg='yellow', bold=True),
        testpath=u'{}:{}'.format(filename, lineno),
        fixtures='\n'.join([u'\t{}'.format(click.style(fixture, fg='yellow')) for fixture in unused_fixtures])
    )


@click.command()
@click.argument('path')
@click.option('--ignore', '-i', multiple=True, default=[], help='ignore these unused fixtures')
def list_missing(path, ignore):
    list_unused = ListUnusedFixtures(ignore=ignore)
    pytest.main(['--collect-only', '-p', 'no:terminal', path], plugins=[list_unused])
    for test, unused_fixtures in list_unused.collected:
        if len(unused_fixtures) > 0:
            click.echo(repr_function(test, unused_fixtures))

if __name__ == "__main__":
    list_missing()
