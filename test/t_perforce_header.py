#!/usr/bin/env python

import unittest
from nose.tools import istest
import src.perforce_header as perforce_header
import src.fileutil as fileutil
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
    def replace_header(self):
        doc = perforce_header.Document('path', 'line\n1\nline2\nline3')
        header_args = {'file_name':'my_file.sql', 'current_date':'2013-12-10'}
        doc.replace_header(self.p4_header, '1', **header_args)
        has_file = False
        has_date = False
        for line in fileutil.blocks(str(doc)):
            if re.search('my_file.sql', line):
                has_file = True
            if re.search('2013', line):
                has_date = True
        assert has_file and has_date

    @istest
    def new_document(self):
        doc = perforce_header.Document('path', 'line1\nline2\nline3')
        self.assertEquals(['line1', 'line2', 'line3'], fileutil.blocks(str(doc)))

    @istest
    def has_flower_box(self):
        doc = perforce_header.Document('path', self.p4_header + '\n\nline1\nline2\nline3')
        begins_with_slash_star_plus_any_number_of_stars = '^/\*(\*)+\n'
        contains_any_number_of_lines = '(.*\n)+'
        ends_with_any_number_of_stars_plus_star_slash = '(\*)+\*/$'
        flower_pattern = begins_with_slash_star_plus_any_number_of_stars + contains_any_number_of_lines + ends_with_any_number_of_stars_plus_star_slash

        matching_patterns = ['/**\n header line one \n**/', '/**********\n header line 1 \n header line 2 \n**************/']
        not_matching_patterns = ['', '*', '/* block comment \n line2 */']
        print flower_pattern
        for txt in matching_patterns:
            assert re.search(flower_pattern, txt), '(' + str(txt) + ')'
        for txt in not_matching_patterns:
            assert not re.search(flower_pattern, txt), '(' + str(txt) + ')'
