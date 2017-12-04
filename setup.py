# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='book_task',
    version='0.1',
    description='Book home task',
    author='Ivelme',
    author_email='ivelmey@gmail.com',
    url='https://example.com',
    packages=find_packages(),
    install_requires=[
        'django == 2.0',
        'mysqlclient == 1.3.12',
    ],
)
