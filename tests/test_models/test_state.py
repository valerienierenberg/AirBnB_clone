#!/usr/bin/python3
""" Unittests for Amenity class and all its attributes and methods
"""
import unittest
import pep8
import json
import sys
import os
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Tests State Class """

    def test_state(self):
        """ tests making instance of State class, tests class attributes """
        myobj = State()
        self.assertIsInstance(myobj, BaseModel)
        self.assertIsInstance(myobj, State)
        self.assertTrue(hasattr(myobj, "id"))
        self.assertTrue(hasattr(myobj, "created_at"))
        self.assertTrue(hasattr(myobj, "updated_at"))
        self.assertTrue(hasattr(myobj, "name"))
        # test if State class attribute was inherited by myobj
        self.assertEqual(State.name, "")
        self.assertEqual(myobj.name, "")
