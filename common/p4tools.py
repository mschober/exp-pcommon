#!/usr/bin/env python
import fileutil
import utilities
import re, os

class P4Tools:

    def __init__(self, p4_path):
        self.p4_path = p4_path
        self.p4 = p4(p4_path)

    def __remove_change_information(self, changes):
        #http://www.perforce.com/perforce/doc.current/manuals/p4guide/08_scripting.html
        #Without the banner
        #p4 print -q filespec
        return [ change.split('#')[0] for change in changes ]

    def __execute_p4_command(self, cmd):
        return utilities.execute_command(cmd)

    def traverse_files(self, sub_path='', limit=None):
        changes = self.p4.files(sub_path, limit=limit)
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

    def get_it(self, filename):
        return self.p4.get_it(filename)

    def edit(self, filename):
        self.p4.edit(filename)

    def save(self, filename, file_text):
        file_string = '\n'.join(file_text)
        local_path = self.p4.where(os.path.join(self.p4_path, filename))
        with open(local_path, 'w') as f:
            f.write(file_string)
            f.close()
