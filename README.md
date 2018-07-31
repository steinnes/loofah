# loofah
[![CircleCI](https://circleci.com/gh/steinnes/loofah.svg?style=svg)](https://circleci.com/gh/steinnes/loofah)

A tool to list test fixtures declared but not used in a test:

![image](https://user-images.githubusercontent.com/1097582/43468569-dfb0a932-94d3-11e8-8c99-ef9245ec430f.png)


This tool is actually a pytest plugin, and with some improved packaging could
be installed, and then called via the `py.test` command line.

----


## Features

* Uses the pytest collection to get a list of tests and available fixtures
* Parses the code for each function to determine whether fixture arguments
  are used or not in the test
* Supports a list of "ignored" fixtures, since some fixtures are only used
  to create and tear down a particular context, and might not be used directly
  in the test code



## Installation

You can install `loofah` via `pip`:

    $ pip install loofah


## Usage

Since loofah relies on pytest collecting and being able to execute the tests,
it needs to be run from your normal development shell, and probably installed
in the venv of your project.

So, from your normal development shell, run loofah as you would run your tests:
(ie with any required environment variables or virtual environment enabled, etc)

    $ loofah test/unit
    ...
    test/unit/account_tests.py:10 in test_account_update_requires_login detected 1 unused fixture:
        user
    test/unit/account_tests.py:28 in test_account_locks_after_three_attempts detected 2 unused fixtures:
        user
        monkeypatch


## Why 'loofah' ?

Why name this project after a fruit with fibrous, spongy interior often used to
clean hard-to-reach areas of the human body?  That's a mystery indeed.


## License

Distributed under the terms of the `MIT`_ license, "loofah" is free and open source software

