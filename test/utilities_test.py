import unittest
from nose.tools import istest
from common import utilities
import re

class UtilitiesTest(unittest.TestCase):

    @istest
    def gets_user(self):
        '''Fetches user from linux whoami.'''
        user = utilities.get_user()
        assert type(user) is str
