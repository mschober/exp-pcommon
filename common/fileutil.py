#!/usr/bin/env python
import os
import collections

def path_head(path):
    return os.path.dirname(path)

def path_tail(path):
    return os.path.basename(path)

def path_heads(paths):
    return map(path_head, paths)

def path_tails(paths):
    return map(path_tail, paths)

def find_duplicates(files, lower=False):
    if lower:
        files = utilities.lowercase(files)
    return [ key for key, val in collections.Counter( files ).iteritems() if val > 1 ]

def blocks(file_string, split_line='\n'):
    return file_string.split(split_line)

def whole(file_lst, join_string='\n'):
    return join_string.join(file_lst)

def lower_line(file_lst, line):
    upper_line = line.upper()
    if not upper_line in file_lst:
        raise ValueError("couldn't find %s in %s" % (file_lst, line))
    text = whole(file_lst).replace(upper_line, line)
    return blocks(text)

class ListFile:

    def __init__(self, file_lines):
        self.file_lines = file_lines

    def file_break(self, width):
        file_separator_string = (width/2 * '=' + '[ FILE BREAK ]' + width/2 * '=')
        return file_separator_string.join(map("\n".join, self.file_lines))
