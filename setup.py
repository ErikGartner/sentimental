#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of sentimental.
# https://github.com/ErikGartner/sentimental

# Licensed under the - license:
# http://www.opensource.org/licenses/--license
# Copyright (c) 2016, Erik Gärtner <erik@gartner.io>

from setuptools import setup, find_packages
from sentimental import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='sentimental',
    version=__version__,
    description='A sentiment analyzer',
    long_description='''
A sentiment analyzer
''',
    keywords='sentiment',
    author='Erik Gärtner',
    author_email='erik@gartner.io',
    url='https://github.com/ErikGartner/sentimental',
    license='-',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: - License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'numpy>=1.11.0',
        'scipy>=0.17.0',
        'scikit-learn>=0.17.1'
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'sentimental=sentimental.cli:main',
        ],
    },
)
