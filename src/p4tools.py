#!/usr/bin/env python
import subprocess
import fileutil

class P4Tools:

    def __init__(self, p4_path):
        self.p4_path = p4_path

    def __remove_change_information(self, changes):
        return [ change.split('#')[0] for change in changes ]

    def __execute_p4_command(self, cmd):
        results = subprocess.check_output(cmd.split()).split('\n')
        results.pop()
        return results

    def traverse_files(self, sub_path=None):
        cmd = "p4 files %s" % (self.p4_path + "/..." + sub_path)
        changes = self.__execute_p4_command(cmd)
        paths = self.__remove_change_information(changes)
        return paths

    def traverse_top_level_dirs(self):
        cmd = "p4 dirs %s" % (self.p4_path + "/*")
        dirs = self.__execute_p4_command(cmd)
        return dirs

    def files_from_sub_dir(self, p4_path):
        return self.traverse_files(p4_path + "/*")

    def to_map(self):
        paths = self.traverse_files()
        sub_paths = [ path.replace(self.p4_path + "/", '') for path in paths ]
        files = fileutil.path_tails(sub_paths)
        keys = '_'.join(fileutil.path_heads(sub_paths))
        path_file = dict(zip(files, keys))
        return path_file

