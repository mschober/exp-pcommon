#!/usr/bin/env python

from nose.tools import istest
import unittest
import common.src.fileutil as fileutil

class TestFileutil(unittest.TestCase):

    @istest
    def lower_line_exception(self):
        a_file = ['line1', 'line2', '/**********', 'comment line1', 'comment line2', '*********/', 'body line 1', 'oops SET NOCOUNT ON', 'body line 3']
        self.assertRaises(ValueError, fileutil.lower_line, a_file, 'set nocount on')

    @istest
    def lower_line_happy_path(self):
        a_file_lst = ['line1', 'line2', '/**********', 'comment line1', 'comment line2', '*********/', 'body line 1', 'SET NOCOUNT ON', 'body line 3']
        file_lowered = fileutil.lower_line(a_file_lst, 'set nocount on')
        self.assertEquals([ a.lower() for a in a_file_lst ], file_lowered)
