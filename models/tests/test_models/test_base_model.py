#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import pep8

'''
TestBaseModel - Unittest for base_model
'''

class TestBaseModel(unittest.TestCase):
    def test_uuid(self)
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasAttribute(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)