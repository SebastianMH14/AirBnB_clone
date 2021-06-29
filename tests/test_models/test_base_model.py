#!/usr/bin/python3
"""
TestBaseModel - Unittest for base_model
"""
import unittest
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    def test_uuid(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasAttribute(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
