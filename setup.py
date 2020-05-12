#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Beam - pyodbc Connector for setup file."""
import re
from pathlib import Path
from typing import List

from setuptools import setup


def get_version(package: str) -> str:
    """
    Return package version as listed in `__version__` in `__version__.py`.
    :param package: package name
    :return: version number
    """
    version = Path(package, '__version__.py').read_text()
    return re.search(r'__version__ = [\'"]([^\'"]+)[\'"]', version).group(1)


def get_long_description() -> str:
    """
    Return the README.
    :return: descrption
    """
    with open('README.md', encoding='utf8') as f:
        return f.read()


def get_packages(package: str) -> List[str]:
    """
    Return root package and all sub-packages.
    :param package: root package
    :return: list of all root packages
    """
    return [str(path.parent) for path in Path(package).glob('**/__init__.py')]


PROJECT_HOME_PAGE = 'https://github.com/314e/beam-pyodbc-connector'

setup(
        namme='beam-pyodbc-connector',
        version=get_version('beam-pyodbc'),
        description='pyodbc I/O Connector for Apache Beam',
        long_description=get_long_description(),
        long_description_content_type='text/markdown',
        url=PROJECT_HOME_PAGE,
        project_urls={
            'Bug Tracker': f'{PROJECT_HOME_PAGE}/issues',
            'Documentation': PROJECT_HOME_PAGE,
            'Source Code': PROJECT_HOME_PAGE
        }

)
