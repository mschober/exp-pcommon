#!/usr/bin/env python

def lowercase(x):
    return map(str.lower, x)

def full_path(*args):
    return "/".join(*args)

def full_paths(path_list):
    return map(full_path, path_list)

