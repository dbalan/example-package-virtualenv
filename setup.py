# -*- coding: utf-8 -*-
# Copyright (c) 2014 Plivo Team. See LICENSE file for details.

from setuptools import setup


setup(
    name='example_package_virtualenv',
    version='1.0',
    url='http://github.com/dbalan/example-package-virtualenv',
    author='dhananjay',
    author_email='dj@inflo.ws',
    packages=['example_package_virtualenv'],
    scripts=['bin/foobar'],
    description=('example python package'),
    long_description=open('README.md').read(),
    install_requires=[
        "gevent",
    ],
)
