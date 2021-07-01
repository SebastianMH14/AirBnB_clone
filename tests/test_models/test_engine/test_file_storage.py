#!/usr/bin/python3
"""file storage test"""
import unittest
from models.engine.file_storage import FileStorage

class FileStorage_test(unittest.TestCase):
    """test file storage"""

    def all_test(self):
        """test all funtions"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertTrue(len(FileStorage.new.__doc__) > 0)
        self.assertTrue(len(FileStorage.all.__doc__) > 0)
        self.assertTrue(len(FileStorage.a.__doc__) > 0)
        self.assertTrue(len(FileStorage.all.__doc__) > 0)