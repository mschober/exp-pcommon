#!/usr/bin/env python

class Document:

    def __init__(self, text):
        #self.text = text.format(**kwargs)
        self.text = text

    def __str__(self):
        return self.text

    def lst(self):
        return self.text.split('\n')

    def replace_header(self, new_header, split_string, **kwargs):
        rebuilt_file = []
        blocks = self.text.split(split_string)

        header_string = blocks[0]
        body_lst = ''.join(blocks[1:]).split('\n')

        header_string = new_header.format(**kwargs)
        header_lst = header_string.split('\n')
        header_lst.append(split_string)

        rebuilt_file.extend(header_lst)
        rebuilt_file.extend(body_lst)
        self.text = "\n".join(rebuilt_file)
