#!/usr/bin/python3
""" Unittests for console class and all its attributes and methods
"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import json
import sys
import os
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ Tests Console Class """

    def test_create(self):
        """ Tests console method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create NOPE")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_destroy(self):
        """ Tests console method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy NOPE")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show(self):
        """ Tests console method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show NOPE")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_all(self):
        """ Tests console method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all NOPE")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_update(self):
        """ Tests console method """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update NOPE")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
