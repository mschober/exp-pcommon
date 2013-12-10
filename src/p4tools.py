#!/usr/bin/env python
import subprocess
import fileutil


class p4:
    def __init__(self, path):
        self.path = path
        self.dirs_list = []
        self.files_list = []

    def __execute_p4_command(self, cmd):
        results = subprocess.check_output(cmd.split()).split('\n')
        results.pop()
        return results

    def dirs(self, sub_path=''):
        cmd = "p4 dirs %s" % ('/'.join([ path for path in [self.path, sub_path, '*'] if path ]))
        self.dirs_list = self.__execute_p4_command(cmd)
        return list(self.dirs_list)

    def files(self, sub_path=''):
        cmd = "p4 files %s" % ('/'.join([ path for path in [self.path, sub_path, '...'] if path ]))
        self.files_list = self.__execute_p4_command(cmd)
        return list(self.files_list)

    def text(self, sub_path=''):
        cmd = 'p4 print %s' % ('/'.join([ path for path in [self.path, sub_path, '*'] if path ]))
        self.files_txt = self.__execute_p4_command(cmd)
        return list(self.files_txt)

class P4Tools:

    def __init__(self, p4_path):
        self.p4_path = p4_path
        self.p4 = p4(p4_path)

    def __remove_change_information(self, changes):
        return [ change.split('#')[0] for change in changes ]

    def __execute_p4_command(self, cmd):
        results = subprocess.check_output(cmd.split()).split('\n')
        results.pop()
        return results

    def traverse_files(self, sub_path=''):
        changes = self.p4.files(sub_path)
        paths = self.__remove_change_information(changes)
        return paths

    def traverse_top_level_dirs(self):
        dirs = self.p4.dirs()
        return dirs

    def files_from_sub_dir(self, *args):
        file_path = self.traverse_files('*/' + args[0])
        file_name = fileutil.path_tails(file_path)
        file_lst = map(self.__execute_p4_command, [ 'p4 print %s' % fpath for fpath in file_path ])
        a_file = zip(file_path, file_lst)
        files = dict(zip(file_name, a_file))
        return files

    def to_map(self):
        paths = self.traverse_files()
        sub_paths = [ path.replace(self.p4_path + "/", '') for path in paths ]
        files = fileutil.path_tails(sub_paths)
        keys = '_'.join(fileutil.path_heads(sub_paths))
        path_file = dict(zip(files, keys)) #this looks backwards because it is, the files are now the keys and the keys are the values
        return path_file
