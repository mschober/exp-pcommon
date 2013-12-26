#!/usr/bin/env python
import subprocess

def lowercase(x):
    return map(str.lower, x)

def full_path(*args):
    return "/".join(*args)

def full_paths(path_list):
    return map(full_path, path_list)

def execute_command(cmd):
    output = subprocess.check_output(cmd.split())
    if len(output) > 1:
        if not output[-1] == '\n':
            output += '\n'
    results = output.split('\n')
    results.pop()
    return results
