#!/usr/bin/python3
"""file storage test"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import pep8


class FileStorage_test(unittest.TestCase):
    """test file storage"""

    def all_test(self):
        """test all funtions"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertTrue(len(FileStorage.new.__doc__) > 0)
        self.assertTrue(len(FileStorage.all.__doc__) > 0)
        self.assertTrue(len(FileStorage.a.__doc__) > 0)
        self.assertTrue(len(FileStorage.all.__doc__) > 0)

    def test_pep8_user(self):
        """test pep8s"""
        style = pep8.StyleGuide(quiet=True)
        v = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(v.total_errors, 0, "fix pep8")
