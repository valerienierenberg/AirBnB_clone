#!/usr/bin/python3
""" Unittests for Amenity class and all its attributes and methods
"""
import unittest
import pep8
import json
import sys
import os
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """ Tests City Class """

    def test_city(self):
        """ tests making instance of City class, tests class attributes """
        myobj = City()
        self.assertIsInstance(myobj, BaseModel)
        self.assertIsInstance(myobj, City)
        self.assertTrue(hasattr(myobj, "id"))
        self.assertTrue(hasattr(myobj, "created_at"))
        self.assertTrue(hasattr(myobj, "updated_at"))
        self.assertTrue(hasattr(myobj, "name"))
        # test if City class attribute was inherited by myobj
        self.assertEqual(City.name, "")
        self.assertEqual(myobj.name, "")
        self.assertEqual(City.state_id, "")
        self.assertEqual(myobj.state_id, "")
