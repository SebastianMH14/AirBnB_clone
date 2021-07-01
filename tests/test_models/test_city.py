#!/usr/bin/python3
"""city test"""

from models.base_model import BaseModel
import unittest
from models.city import City
import pep8


class User_test(unittest.TestCase):
    """city test"""
    def test_pep8_user(self):
        """test pep8s"""
        style = pep8.StyleGuide(quiet=True)
        v = style.check_files(['models/city.py'])
        self.assertEqual(v.total_errors, 0, "fix pep8")
