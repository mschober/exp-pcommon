#!/usr/bin/env python

from nose.tools import istest
import src.p4tools as p4tools
import unittest

class Testp4(unittest.TestCase):

    @istest
    def dirs_cmd_happy_path(self):
        p4 = p4tools.p4('//depot/dmo/*')
        self.assertEquals('', p4.dirs()[0].split('//depot/dmo')[0])
