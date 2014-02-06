import pytest, unittest
from common import p4_files

class P4FilesTest(unittest.TestCase):

    def test_depot_path_to_key(self):
        depot_path = '//depot/EDW/PRODEDW'
        assert p4_files.depot_path_to_key(depot_path) == '__depot_EDW_PRODEDW'
