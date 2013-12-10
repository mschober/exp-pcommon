#!/usr/bin/env python

import unittest
from nose.tools import istest
import src.perforce_header as perforce_header
import re

class TestDocument(unittest.TestCase):

    p4_header = '''/******************************************************************************
Copyright 2013 Expedia, Inc.

Description:
   This script creates the PK for the {file_name} table

Change History:
    Date        Author               Description
    ----------  ---------------      ------------------------------------
    {current_date}  Booking Engineering  Created

******************************************************************************/'''

    @istest
    def my_example(self):
        doc = perforce_header.Document('line1\nline2\nline3')
        doc.replace_header(self.p4_header, '1', file_name='my_file.sql', current_date='2013-12-10')
        has_file = False
        has_date = False
        for line in doc.lst():
            if re.search('my_file.sql', line):
                has_file = True
        for line in doc.lst():
            if re.search('2013', line):
                has_date = True
        assert has_file and has_date

    @istest
    def new_document(self):
        doc = perforce_header.Document('line1\nline2\nline3')
        self.assertEquals(['line1', 'line2', 'line3'], doc.lst())
