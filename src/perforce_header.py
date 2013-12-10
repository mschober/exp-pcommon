#!/usr/bin/env python

class PerforceHeader:

    def __init__(self, header, **kwargs):
        self.header = header.format(**kwargs)
        self.kwargs = kwargs

    def __str__(self):
        return self.header

    def lst(self):
        return self.header.split('\n')
