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

******************************************************************************/
'''

    @istest
    def replace_header(self):
        doc = perforce_header.Document('path', 'line\n1\nline2\nline3')
        header_args = {'file_name':'my_file.sql', 'current_date':'2013-12-10'}
        doc.replace_header(self.p4_header, **header_args)
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
        matching_patterns = ['/**\n header line one \n**/\n', '/**********\n header line 1 \n header line 2 \n**************/\n']
        not_matching_patterns = ['', '*', '/* block comment \n line2 */']
        for txt in matching_patterns:
            doc = perforce_header.Document('path', txt)
            assert doc.has_flowerbox(), 'matching ({txt})'.format(txt=txt)
        for txt in not_matching_patterns:
            doc = perforce_header.Document('path', txt)
            assert not doc.has_flowerbox(), 'not matching ({txt})'.format(txt=txt)

    @istest
    def flower_box_wrapped_in_block_comment(self):
        matching_patterns = ['/*\n**\n header line one \n**\n*/\n', '/*\n*********\n header line 1 \n header line 2 \n*************\n*/\n']
        for txt in matching_patterns:
            doc = perforce_header.Document('path', txt)
            assert doc.has_flowerbox(), 'matching ({txt})'.format(txt=txt)

    @istest
    def remove_flower_box(self):
        simple = perforce_header.Document('path', self.p4_header + 'line1\nline2\n')
        wrapped_in_block_comment = perforce_header.Document('path', '/*\n*****\ncomment line1\ncomment line2\n*****\n*/\nline1\nline2\n')
        removals = [simple, wrapped_in_block_comment]
        for to_remove in removals:
            self.assertEquals(to_remove.remove_header(), 'line1\nline2\n')


