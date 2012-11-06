# -*- coding: utf-8 -*-
"""
    ks.time.util
    ~~~~~~~~~~~~

    Utility functions for dealing with Pandas timestamps.

    :copyright: (c) 2010 -- 2012 by Charlie Sharpsteen
    :license: BSD

"""

from pandas import date_range, Timestamp
from pandas.tseries.frequencies import to_offset


def split_to_ranges(start, end, freq = 'D', tz = None, round = True):
    """
    Generates a list of intervals that spans a given time period.

    Parameters
    ----------
    start : string or datetime-like,
        Left bound for generating dates
    end : string or datetime-like,
        Right bound for generating dates
    freq : string or DateOffset, default 'D' (calendar daily)
        Frequency strings can have multiples, e.g. '5H'
    tz : string or None
        Time zone name for returning localized DatetimeIndex, for example
        Asia/Beijing
    round: boolean, default True
        specifies whether the end date is rounded up such that the last
        interval is of length 'freq' or left as-is thus generating an irregular
        final interval but allowing the set of intervals to exactly represent
        the timespan between start and end.
    """

    # Coerce start and end to Timestamp objects and freq to a DateOffset object
    start = Timestamp(start)
    end = Timestamp(end)
    freq = to_offset(freq)

    # Calculate timestamps that bracket time periods of length freq.
    breaks = [d for d in date_range(start, end, freq = freq, tz = tz)]

    # Extend if necessary so that the end timestamp is included.
    if breaks[-1] < end:
        if round:
            breaks.append(breaks[-1] + freq)
        else:
            breaks.append(end)

    # Generate the list of intervals.
    return zip(breaks[:-1], breaks[1:])
