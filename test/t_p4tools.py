#!/usr/bin/env python

from nose.tools import istest
import src.p4tools as p4tools

class Testp4:

    @istest
    def dirs_cmd_happy_path(self):
        p4 = p4tools.p4('//depot/dmo')
        assert 'dmo' in p4.dirs()[0].split('/')
