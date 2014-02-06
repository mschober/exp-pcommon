#!/usr/bin/env python

import unittest
from common import fileutil

class TestFileutil(unittest.TestCase):

    def test_lower_line_exception(self):
        a_file = ['line1', 'line2', '/**********', 'comment line1', 'comment line2', '*********/', 'body line 1', 'oops SET NOCOUNT ON', 'body line 3']
        self.assertRaises(ValueError, fileutil.lower_line, a_file, 'set nocount on')

    def test_lower_line_happy_path(self):
        a_file_lst = ['line1', 'line2', '/**********', 'comment line1', 'comment line2', '*********/', 'body line 1', 'SET NOCOUNT ON', 'body line 3']
        file_lowered = fileutil.lower_line(a_file_lst, 'set nocount on')
        self.assertEquals([ a.lower() for a in a_file_lst ], file_lowered)

    def test_path_head(self):
        path = "//depot/EDW/PRODEDW/ADS/bvt/db/tbl/AB_EXPERIMNT_INSTNC_RUN_TYP.sql"
        assert fileutil.path_head(path) == "//depot/EDW/PRODEDW/ADS/bvt/db/tbl"
