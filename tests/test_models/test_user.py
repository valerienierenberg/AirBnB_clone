#!/usr/bin/python3
""" Unittests for Amenity class and all its attributes and methods
"""
import unittest
import pep8
import json
import sys
import os
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """ Tests User Class """

    def test_user(self):
        """ tests making instance of User class, tests class attributes """
        myobj = User()
        self.assertIsInstance(myobj, BaseModel)
        self.assertIsInstance(myobj, User)
        self.assertTrue(hasattr(myobj, "id"))
        self.assertTrue(hasattr(myobj, "created_at"))
        self.assertTrue(hasattr(myobj, "updated_at"))
        # test if User class attribute was inherited by myobj
        self.assertEqual(User.email, "")
        self.assertEqual(myobj.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(myobj.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(myobj.first_name, "")
        self.assertEqual(User.last_name, "")
        self.assertEqual(myobj.last_name, "")

