from common import p4_connector
import unittest

class TestP4Connector(unittest.TestCase):

    def test_dirs_cmd_happy_path(self):
        path = '//depot/dmo'
        p4 = p4_connector.P4(path)
        self.assertEquals(path.split('/'), p4.dirs()[0].split('/')[0:-1])

    def test_dirs_cmd_with_sub_path(self):
        path = '//depot'
        p4 = p4_connector.P4(path)
        self.assertEquals(path.split('/') + ['dmo'], p4.dirs('dmo')[0].split('/')[0:-1])

    def test_files_cmd_happy_path(self):
        path = '//depot/dmo/BookingImp/BookingImp/DEV/db/tbl/index'
        p4 = p4_connector.P4(path)
        print path
        self.assertEquals(path.split('/'), p4.files()[0].split('/')[0:-1])

    def test_files_cmd_with_sub_path(self):
        path = '//depot/dmo/BookingImp/BookingImp/DEV/db/tbl'
        p4 = p4_connector.P4(path)
        self.assertEquals(path.split('/') + ['index'], p4.files('index')[0].split('/')[0:-1])

    def test_files_cmd_limit(self):
        path = '//depot/EDW/PRODEDW'
        p4 = p4_connector.P4(path)
        assert len(p4.files(limit=5)) == 5

    def test_get_file_with_space_in_path(self):
        pass
