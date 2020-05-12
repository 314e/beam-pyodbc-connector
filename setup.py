#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Beam - pyodbc Connector for setup file."""

from setuptools import setup

PROJECT_HOME_PAGE = 'https://github.com/314e/beam-pyodbc-connector'
DOWNLOAD_URL = 'https://pypi.python.org/pypi/beam-pyodbc-connector'

setup(
        url=PROJECT_HOME_PAGE,
        project_urls={
            'Bug Tracker': f'{PROJECT_HOME_PAGE}/issues',
            'Documentation': PROJECT_HOME_PAGE,
            'Source Code': PROJECT_HOME_PAGE
        },
        download_url=DOWNLOAD_URL,
)
