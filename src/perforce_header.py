#!/usr/bin/env python
import common.src.fileutil as fileutil

class Document:

    def __init__(self, p4_path, text):
        self.path = p4_path
        self.text = text
        self.no_match = []

    def __str__(self):
        return self.text

    def __blocks(self, split_string):
        return self.text.split(split_string)

    def lst(self):
        return self.__blocks('\n')

    def file_name(self):
        return fileutil.path_tail(self.path)

    def p4_path(self):
        return self.path

    def remove_root(self, root):
        fname = fileutil.path_tail(self.path)
        self.path = self.path.replace(root + '/', '')
        self.path = self.path.replace('/' + fname, '')

    def __replace_header(self, new_header, split_string, upper=False, **kwargs):
        rebuilt_file = []

        if upper:
            split_string = str.upper(split_string)

        if split_string in self.lst():
            blocks = self.__blocks(split_string)

            header_string = blocks[0]
            body_lst = ''.join(blocks[1:]).split('\n')

            header_string = new_header.format(**kwargs)
            header_lst = header_string.split('\n')
            header_lst.append(split_string)

            rebuilt_file.extend(header_lst)
            rebuilt_file.extend(body_lst)
            self.text = "\n".join(rebuilt_file)
        else:
            self.no_match.append(self.text)


    def replace_header(self, new_header, split_string, **kwargs):
        self.__replace_header(new_header, split_string, **kwargs)
        self.__replace_header(new_header, split_string, upper=True, **kwargs)
