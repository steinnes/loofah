#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='loofah',
    version='0.1.2',
    author='Steinn Eldjarn Sigurdarson',
    author_email='steinn@takumi.com',
    maintainer='Steinn Eldjarn Sigurdarson',
    maintainer_email='steinn@takumi.com',
    license='MIT',
    url='https://github.com/steinnes/loofah',
    description='A pytest-based tool to list test fixtures declared but not used in a test',
    long_description=read('README.md'),
    py_modules=['loofah'],
    install_requires=['pytest>=3.1.1', 'click>=6.1', 'mock==2.0.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
            'loofah = loofah:list_missing'
        ],
    },
)
