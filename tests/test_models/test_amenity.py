#!/usr/bin/python3
""" Unittests for Amenity class and all its attributes and methods
"""
import unittest
import pep8
import json
import sys
import os
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """ Tests Amenity Class """

    def test_amenity(self):
        """ tests making instance of Amenity class, tests class attributes """
        myobj = Amenity()
        self.assertIsInstance(myobj, BaseModel)
        self.assertIsInstance(myobj, Amenity)
        self.assertTrue(hasattr(myobj, "id"))
        self.assertTrue(hasattr(myobj, "created_at"))
        self.assertTrue(hasattr(myobj, "updated_at"))
        self.assertTrue(hasattr(myobj, "name"))
        # test if Amenity class attribute was inherited by myobj
        self.assertEqual(Amenity.name, "")
        self.assertEqual(myobj.name, "")
