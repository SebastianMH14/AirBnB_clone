#!/usr/bin/python3
"""Review test"""

from models.base_model import BaseModel
import unittest
from models.review import Review
import pep8


class User_test(unittest.TestCase):
    """review test"""
    def test_pep8_user(self):
        """test pep8s"""
        style = pep8.StyleGuide(quiet=True)
        v = style.check_files(['models/review.py'])
        self.assertEqual(v.total_errors, 0, "fix pep8")
