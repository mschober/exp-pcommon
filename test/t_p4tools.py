#!/usr/bin/env python

from nose.tools import istest
import src.p4tools as p4tools

class Testp4:

    @istest
    def examp(self):
        p4 = p4tools.p4('//depot/dmo')
        assert 'dmo' in p4.dirs().split('/')
