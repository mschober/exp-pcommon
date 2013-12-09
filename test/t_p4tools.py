#!/usr/bin/env python

from nose.tools import istest
import src.p4tools as p4tools
import unittest

class Testp4(unittest.TestCase):

    @istest
    def dirs_cmd_happy_path(self):
        path = '//depot/dmo/*'
        p4 = p4tools.p4(path)
        self.assertEquals('', p4.dirs()[0].split(path[:-2])[0])

    @istest
    def files_cmd_happy_path(self):
        path = '//depot/dmo/BookingImp/BookingImp/DEV/db/tbl/index/...'
        p4 = p4tools.p4(path)
        self.assertEquals('', p4.files()[0].split(path[:-4])[0])
