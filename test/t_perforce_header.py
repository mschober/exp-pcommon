#!/usr/bin/env python

import unittest
from nose.tools import istest
import src.perforce_header as perforce_header
import re

class TestPerforceHeader(unittest.TestCase):

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
        header = perforce_header.PerforceHeader(self.p4_header, file_name='my_file.sql', current_date='2013')
        has_file = False
        has_date = False
        for line in header.lst():
            if re.search('my_file.sql', line):
                has_file = True
        for line in header.lst():
            if re.search('2013', line):
                has_date = True
        assert has_file and has_date
