#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of sentimental.
# https://github.com/ErikGartner/sentimental

# Licensed under the - license:
# http://www.opensource.org/licenses/--license
# Copyright (c) 2016, Erik Gärtner <erik@gartner.io>

from setuptools import setup, find_packages
from version import __version__

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
    long_description=
    '''Sentiment analysis made easy; built on top off solid libraries.

Sentimental uses Scikit-learn to perform easy sentiment analysis. The idea is to create a simple out-of-box solution that yields acceptable results without complex configuration. Sentimental also uses a simple format for its training corpora that makes it easy to add more training data.''',
    keywords=['sentiment analysis', 'sentiment', 'nlp'],
    author='Erik Gärtner',
    author_email='erik@gartner.io',
    url='https://github.com/ErikGartner/sentimental',
    download_url='https://github.com/ErikGartner/sentimental/archive/' +
    __version__ + '.tar.gz',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy>=1.11.0',
        'scipy>=0.17.0',
        'scikit-learn>=0.17.1',
        'pyahocorasick>=1.1.0',
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'sentimental=sentimental.cli:main',
        ],
    }, )
