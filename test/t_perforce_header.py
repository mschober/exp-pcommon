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

    p4_body = 'line1\nline2\n'

    p4_header_case_study ='''
/*   
*********************************************************************   
Copyright (C) 2010 Expedia, Inc. 
All rights reserved. 

Name: TravelerAccountRewardEventType.sql 

Description: 
    Create the TravelerAccountRewardEventType table. 

Change History: 
    Date        Author          Description 
    ----------  --------------- ------------------------------------ 
    20100104    v-smvasilik     Created 

*********************************************************************   
*/   '''
    p4_body_case_study = '''

go 

GO 



'''

    @istest
    def replace_header(self):
        doc = perforce_header.Document('path', self.p4_body)
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
        doc = perforce_header.Document('path', self.p4_body)
        self.assertEquals(['line1', 'line2', ''], fileutil.blocks(str(doc)))

    @istest
    def has_flowerbox(self):
        matching_patterns = ['/**\n header line one \n**/\n', '/**********\n header line 1 \n header line 2 \n**************/\n']
        not_matching_patterns = ['', '*', '/* block comment \n line2 */']
        for txt in matching_patterns:
            doc = perforce_header.Document('path', txt)
            assert doc.has_flowerbox(), 'matching ({txt})'.format(txt=txt)
        for txt in not_matching_patterns:
            doc = perforce_header.Document('path', txt)
            assert not doc.has_flowerbox(), 'not matching ({txt})'.format(txt=txt)

    @istest
    def flowerbox_wrapped_in_block_comment(self):
        matching_patterns = ['/*\n**\n header line one \n**\n*/\n', '/*\n*********\n header line 1 \n header line 2 \n*************\n*/\n']
        for txt in matching_patterns:
            doc = perforce_header.Document('path', txt)
            assert doc.has_flowerbox(), 'matching ({txt})'.format(txt=txt)

    @istest
    def remove_flowerbox(self):
        simple = perforce_header.Document('path', self.p4_header + self.p4_body)
        wrapped_in_block_comment = perforce_header.Document('path', '/*\n*****\ncomment line1\ncomment line2\n*****\n*/\n' + self.p4_body)
        removals = [simple, wrapped_in_block_comment]
        for to_remove in removals:
            self.assertEquals(str(to_remove.remove_header()), self.p4_body)

    @istest
    def remove_flowerbox_with_text_above(self):
        starts_with_space = perforce_header.Document('path', ' \n' + self.p4_header + self.p4_body)
        self.assertEquals(str(starts_with_space.remove_header()), ' \n' + self.p4_body)

    @istest
    def remove_flowerbox_case_study(self):
        case_study = perforce_header.Document('path', self.p4_header_case_study + self.p4_body_case_study)
        self.assertEquals(self.p4_body_case_study, str(case_study.remove_header()))

    @istest
    def remove_flowerbox_does_not_delete_to_end_of_next_comment_block(self):
        has_block_comment = perforce_header.Document('path', self.p4_header_case_study + self.p4_body_case_study + '/*\n' + self.p4_body + '*/\nline3\nline4\n')
        self.assertEquals(self.p4_body_case_study + '/*\n' + self.p4_body + '*/\nline3\nline4\n', str(has_block_comment.remove_header()))
