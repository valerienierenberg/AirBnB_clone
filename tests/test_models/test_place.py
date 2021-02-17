#!/usr/bin/python3
""" Unittests for Amenity class and all its attributes and methods
"""
import unittest
import pep8
import json
import sys
import os
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Tests Place Class """

    def test_place(self):
        """ tests making instance of Place class, tests class attributes """
        myobj = Place()
        self.assertIsInstance(myobj, BaseModel)
        self.assertIsInstance(myobj, Place)
        self.assertTrue(hasattr(myobj, "id"))
        self.assertTrue(hasattr(myobj, "created_at"))
        self.assertTrue(hasattr(myobj, "updated_at"))
        self.assertTrue(hasattr(myobj, "name"))
        # test if Place class attribute was inherited by myobj
        self.assertEqual(Place.name, "")
        self.assertEqual(myobj.name, "")
        self.assertEqual(Place.city_id, "")
        self.assertEqual(myobj.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(myobj.user_id, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(myobj.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(myobj.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(myobj.number_bathrooms, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(myobj.price_by_night, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(myobj.max_guest, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(myobj.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(myobj.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
        self.assertEqual(myobj.amenity_ids, [])
