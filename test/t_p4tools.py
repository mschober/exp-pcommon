#!/usr/bin/env python

from nose.tools import istest
import src.p4tools as p4tools
import unittest

class Testp4(unittest.TestCase):

    @istest
    def dirs_cmd_happy_path(self):
        path = '//depot/dmo'
        p4 = p4tools.p4(path)
        self.assertEquals(path.split('/'), p4.dirs()[0].split('/')[0:-1])

    @istest
    def dirs_cmd_with_sub_path(self):
        path = '//depot'
        p4 = p4tools.p4(path)
        self.assertEquals(path.split('/') + ['dmo'], p4.dirs('dmo')[0].split('/')[0:-1])

    @istest
    def files_cmd_happy_path(self):
        path = '//depot/dmo/BookingImp/BookingImp/DEV/db/tbl/index'
        p4 = p4tools.p4(path)
        print path
        self.assertEquals(path.split('/'), p4.files()[0].split('/')[0:-1])

    @istest
    def files_cmd_with_sub_path(self):
        path = '//depot/dmo/BookingImp/BookingImp/DEV/db/tbl'
        p4 = p4tools.p4(path)
        self.assertEquals(path.split('/') + ['index'], p4.files('index')[0].split('/')[0:-1])
