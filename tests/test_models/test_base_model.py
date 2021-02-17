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

    def test_init_base_model(self):
        """ tests __init__ method of BaseModel """
        myobj = BaseModel()
        test1 = str(myobj)
        self.assertTrue(test1[:50], 'models.base_model.BaseModel object at ')
        self.assertTrue(hasattr(myobj, "__init__"))
        self.assertTrue(hasattr(myobj, "__str__"))
        self.assertTrue(hasattr(myobj, "save"))
        self.assertTrue(hasattr(myobj, "to_dict"))
#        __objects = storage.all()

    def test_str_(self):
        """ test that str method for BaseModel class prints correct
        string format """
        bm1 = BaseModel()
        self.assertEqual(bm1.__str__(), "[BaseModel] ({}) {}".
                         format(bm1.id, bm1.__dict__))
#        r2 = Rectangle(2, 3, 2, 2)
#        self.assertEqual(r2.__str__(), "[Rectangle] (1) 2/2 - 2/3")
