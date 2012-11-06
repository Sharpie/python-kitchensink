# -*- coding: utf-8 -*-
"""
    ks.path.utils
    ~~~~~~~~~~~~~

    General-purpose path manipulation utilities.

    :copyright: (c) 2012 by Charlie Sharpsteen
    :license: MIT

"""

import errno
import fnmatch
import os

def dir_glob(pattern, root=os.curdir):
    '''Recursive glob similar to ZSH's ** operator '''
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)

def mkpath(a_path):
    """Like mkdir, but doesn't throw an error if the directory allready exists"""
    try:
        os.makedirs(a_path)
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            pass
        else: raise
