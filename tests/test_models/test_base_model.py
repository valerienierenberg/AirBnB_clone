#!/usr/bin/python3
""" Unittests for BaseModel class and all its attributes and methods
"""
import unittest
import pep8
import json
import sys
import os
from models.base_model import BaseModel
from models.amenity import Amenity

class TestBase(unittest.TestCase):
    """ Tests BaseModel Class """

    def test_documentation(self):
        """
        Test that all methods exist, contain correct documentation
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(BaseModel.__str__.__doc__)
        self.assertTrue(BaseModel.save.__doc__)
        self.assertTrue(BaseModel.to_dict.__doc__)
