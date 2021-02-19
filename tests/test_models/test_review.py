#!/usr/bin/python3
""" Unittests for Amenity class and all its attributes and methods
"""
import json
from models.base_model import BaseModel
from models.review import Review
import os
import pep8
import sys
import unittest


class TestReview(unittest.TestCase):
    """ Tests Review Class """

    def test_review(self):
        """ tests making instance of Review class, tests class attributes """
        myobj = Review()
        self.assertIsInstance(myobj, BaseModel)
        self.assertIsInstance(myobj, Review)
        self.assertTrue(hasattr(myobj, "id"))
        self.assertTrue(hasattr(myobj, "created_at"))
        self.assertTrue(hasattr(myobj, "updated_at"))
        # test if Review class attribute was inherited by myobj
        self.assertEqual(Review.place_id, "")
        self.assertEqual(myobj.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(myobj.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertEqual(myobj.text, "")
