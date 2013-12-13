#!/usr/bin/env python

from nose.tools import istest
import unittest
import common.src.fileutil as fileutil

class TestFileutil(unittest.TestCase):

    @istest
    def lower_line(self):
        a_file = '\n'.join(['line1', 'line2', '/**********', 'comment line1', 'comment line2', '*********/', 'body line 1', 'SET NOCOUNT ON', 'body line 3'])
        file_lowered = fileutil.lower_line(a_file, 'set nocount on')
        self.assertEquals(a_file, file_lowered)

