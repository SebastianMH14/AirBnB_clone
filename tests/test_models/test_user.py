#!/usr/bin/python3
"""User test"""

from models.base_model import BaseModel
import unittest
from models.user import User
import pep8


class User_test(unittest.TestCase):
    """user test"""
    def test_pep8_user(self):
        """test pep8s"""
        style = pep8.StyleGuide(quiet=True)
        v = style.check_files(['models/user.py'])
        self.assertEqual(v.total_errors, 0, "fix pep8")
