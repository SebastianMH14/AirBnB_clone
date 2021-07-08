#!/usr/bin/python3
"""State test"""

from models.base_model import BaseModel
import unittest
from models.state import State
import pep8


class User_test(unittest.TestCase):
    """state test"""
    def test_pep8_user(self):
        """test pep8s"""
        style = pep8.StyleGuide(quiet=True)
        v = style.check_files(['models/state.py'])
        self.assertEqual(v.total_errors, 0, "fix pep8")
