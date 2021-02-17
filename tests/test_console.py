#!/usr/bin/python3
""" Unittests for console class and all its attributes and methods
"""
import unittest
import pep8
import json
import sys
import os
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ Tests Console Class """

    def test_console(self):
        """ Tests console method """
