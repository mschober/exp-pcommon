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

    def __lst(self):
        return fileutil.blocks(self.text)

    def file_name(self):
        return fileutil.path_tail(self.path)

    def remove_root(self, root):
        fname = fileutil.path_tail(self.path)
        self.path = self.path.replace(root + '/', '')
        self.path = self.path.replace('/' + fname, '')

    def missing(self):
        return self.no_match

    def has_flowerbox(self):
        begins_with_slash_star_plus_any_number_of_stars = '^/\*(\*)+\n'
        contains_any_number_of_lines = '(.*\n)+'
        ends_with_any_number_of_stars_plus_star_slash = '(\*)+\*/$'
        flower_pattern = begins_with_slash_star_plus_any_number_of_stars + contains_any_number_of_lines + ends_with_any_number_of_stars_plus_star_slash
        return re.search(flower_pattern, self.text)

    def __replace_header(self, new_header, split_line=None, upper=False, **kwargs):

        if not split_line:
            header_string = new_header.format(**kwargs)
            body_string = self.text
            self.text = fileutil.whole([header_string, 'set nocount on', body_string])
        elif re.search(split_line, self.text):
            split_line = split_line.replace('\*', '*')
            split_line if not upper else split_line.upper()
            blocks = fileutil.blocks(self.text, split_line)
            header_string = new_header.format(**kwargs)
            body_string = fileutil.whole(blocks[1:])
            self.text = fileutil.whole([header_string, 'set nocount on', body_string])
        else:
            self.no_match = (self.path, self.text)

    def replace_header(self, new_header, split_line=None, **kwargs):
        missing = self.__replace_header(new_header, split_line, **kwargs)
        missing = missing and self.__replace_header(new_header, split_line, upper=True, **kwargs)
        if missing:
            self.no_match = (self.path, self.text)
