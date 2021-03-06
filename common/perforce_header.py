#!/usr/bin/env python
import fileutil
import re

class Document:
    __BEGINS_WITH_SLASH_STAR_PLUS_ANY_NUMBER_OF_STARS = '/\*( +)?\n?(\*)+( +)?\n'
    __CONTAINS_ANY_NUMBER_OF_LINES = '(.*\n)+'
    __ENDS_WITH_ANY_NUMBER_OF_STARS_PLUS_STAR_SLASH = '(\*)+( +)?\n?\*/( +)?\n?'
    __FLOWER_PATTERN = __BEGINS_WITH_SLASH_STAR_PLUS_ANY_NUMBER_OF_STARS + __CONTAINS_ANY_NUMBER_OF_LINES + __ENDS_WITH_ANY_NUMBER_OF_STARS_PLUS_STAR_SLASH
    FLOWER_PATTERN_REGEX = re.compile(__FLOWER_PATTERN)


    def __init__(self, p4_path, text):
        self.path = p4_path
        self.text = text

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

    def has_flowerbox(self):
        return self.FLOWER_PATTERN_REGEX.match(self.text)

    def __insert_header(self, new_header, **kwargs):
        header_string = new_header.format(**kwargs)
        body_string = self.text
        self.text = fileutil.whole([header_string, 'set nocount on', body_string])
        return self

    def remove_header(self):
        self.text = re.sub(self.FLOWER_PATTERN_REGEX, '', self.text)
        return self

    def replace_header(self, new_header, **kwargs):
        self.remove_header()
        self.__insert_header(new_header, **kwargs)
        return self
