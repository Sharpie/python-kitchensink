# -*- coding: utf-8 -*-
"""
    ks.path.context
    ~~~~~~~~~~~~~~~

    Context managers for working with paths.

    :copyright: (c) 2012 by Charlie Sharpsteen
    :license: MIT
"""


import errno
import fnmatch
import os
from contextlib import contextmanager, closing

@contextmanager
def cd(dirname=None):
    """Temporarily shift to a new directory"""
    curdir = os.getcwd()
    try:
        if dirname is not None:
            os.chdir(dirname)
        yield os.getcwd()
    finally:
        os.chdir(curdir)
