#!/usr/bin/env python
import os
import collections

def path_head(path):
    return os.path.split(path)[0]

def path_tail(path):
    return os.path.split(path)[1]

def path_heads(paths):
    return map(path_head, paths)

def path_tails(paths):
    return map(path_tail, paths)

def find_duplicates(files, lower=False):
    if lower:
        files = utilities.lowercase(files)
    return [ key for key, val in collections.Counter( files ).iteritems() if val > 1 ]
