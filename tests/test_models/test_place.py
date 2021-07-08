#!/usr/bin/python3
"""Place test"""

from models.base_model import BaseModel
import unittest
from models.place import Place
import pep8


class User_test(unittest.TestCase):
    """place test"""
    def test_pep8_user(self):
        """test pep8s"""
        style = pep8.StyleGuide(quiet=True)
        v = style.check_files(['models/place.py'])
        self.assertEqual(v.total_errors, 0, "fix pep8")
