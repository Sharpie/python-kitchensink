# -*- coding: utf-8 -*-
"""
    ks.time
    ~~~~~~~

    General tools for manipulation of time objects. Enhanced by Pandas.

    :copyright: (c) 2012 -- by Charlie Sharpsteen
    :license: MIT

"""

try:
    from ._pandas import split_to_ranges
except ImportError:
    pass

from ._util import from_isostring, to_posix
