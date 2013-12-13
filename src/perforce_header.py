#!/usr/bin/env python
import common.src.fileutil as fileutil
import re

class Document:

    def __init__(self, p4_path, text):
        self.path = p4_path
        self.text = text
        self.no_match = []

    def __str__(self):
        return self.text

    def __blocks(self, split_line):
        return self.text.split(split_line)

    def lst(self):
        return self.__blocks('\n')

    def file_name(self):
        return fileutil.path_tail(self.path)

    def remove_root(self, root):
        fname = fileutil.path_tail(self.path)
        self.path = self.path.replace(root + '/', '')
        self.path = self.path.replace('/' + fname, '')

    def missing(self):
        return self.no_match

    def __replace_header(self, new_header, split_line=None, upper=False, **kwargs):
        rebuilt_file = []

        def insert_header(new_header, **kwargs):
            header_string = new_header.format(**kwargs)
            header_lst = header_string.split('\n')
            header_lst.append(split_line)

            rebuilt_file.extend(header_lst)
            rebuilt_file.extend(body_lst)
            self.text = "\n".join(rebuilt_file)


        if not split_line:
            pass
            #insert_header(new_header, **kwargs)

        if upper:
            split_line = str.upper(split_line)

        if split_line in self.lst():
            blocks = self.__blocks(split_line)

            if len(blocks[0]) < 3 and re.search(r'/' + 5 * '\*', blocks[1]):
                print 'split wrong, blocks (%s) path (%s)' % (blocks[0], self.path)

            header_string = blocks[0]
            body_lst = ''.join(blocks[1:]).split('\n')

            insert_header(new_header, **kwargs)
            return False
        else:
            return True


    def replace_header(self, new_header, split_line, **kwargs):
        missing = self.__replace_header(new_header, split_line, **kwargs)
        missing = missing and self.__replace_header(new_header, split_line, upper=True, **kwargs)
        if missing:
            self.no_match = (self.path, self.text)
