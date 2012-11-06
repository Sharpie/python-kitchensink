# -*- coding: utf-8 -*-
"""
    ks.time.util
    ~~~~~~~~~~~~

    Misc. utility functions for dealing with time.

    :copyright: (c) 2010 -- 2012 by Charlie Sharpsteen
    :license: BSD

"""

import time
from datetime import datetime, timedelta


def from_isostring(datestring):
    """Takes a string in 'unambiguous format' and returns a datetime object.
    Here, 'unambiguous format' is arbitrarily declared to be a subset of the
    ISO 8601 format:

        %Y-%m-%d %H:%M:%S
    """
    return datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S')

def to_posix(dt):
    """Converts a time object to seconds since the UNIX epoch."""
    return time.mktime(dt.timetuple())
