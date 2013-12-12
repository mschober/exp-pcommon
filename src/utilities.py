#!/usr/bin/env python
import subprocess

def lowercase(x):
    return map(str.lower, x)

def full_path(*args):
    return "/".join(*args)

def full_paths(path_list):
    return map(full_path, path_list)

def execute_command(cmd):
    results = subprocess.check_output(cmd.split()).split('\n')
    results.pop()
    return results
