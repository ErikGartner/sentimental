#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of sentimental.
# https://github.com/ErikGartner/sentimental

# Licensed under the - license:
# http://www.opensource.org/licenses/--license
# Copyright (c) 2016, Erik Gärtner <erik@gartner.io>
import os

from version import __version__  # NOQA
from sentimental.sentimental import Sentimental
from sentimental.example_extractor import ExampleExtractor


def get_data_path():
    return os.path.dirname(__file__) + '/data'
