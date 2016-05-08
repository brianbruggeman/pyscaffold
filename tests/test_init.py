#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pkg_resources
import pyscaffold

__author__ = 'Brian Bruggeman'
__copyright__ = '2016'
__license__ = 'Apache 2.0'


def test_version():
    version = pyscaffold.__version__.split(".")
    assert int(version[0]) >= 0


def test_unknown_version(get_distribution_raises_exception):  # noqa
    version = pyscaffold.__version__
    assert version == 'unknown'
