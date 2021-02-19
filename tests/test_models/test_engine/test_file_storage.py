#!/usr/bin/python3
""" Unittests for file_storage and all its attributes and methods
"""
import json
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pep8
import os
from os.path import exists
import sys
import unittest


class TestFileStorage(unittest.TestCase):
    """ Tests File_Storage Class """

    def FileStorage(self):
        """ tests for file_storage """
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))
        self.assertTrue(FileStorage.all.__doc__)
        self.assertTrue(FileStorage.new.__doc__)
        self.assertTrue(FileStorage.save.__doc__)
        self.assertTrue(FileStorage.reload.__doc__)

    def test_all(self):
        """ tests all method of file_storage """
        myobj = BaseModel()
        __objects = storage.all()

    def test_new(self):
        """ tests new method of file_storage """
        myobj = BaseModel()
        #  store myobj into __objects variable by <class name>.id using new()
        __objects = storage.new(myobj)

    def test_save(self):
        """ tests save method of file_storage """
        __file_path = "file.json"
        storage.save()
        #  check if file.json file was created by save method
        self.assertTrue(exists(__file_path))

    def test_reload(self):
        """ tests reload method of file_storage """
        myobj = BaseModel()
        __objects = storage.all()
        storage.reload()
        __objects_reloaded = storage.all()
        self.assertEqual(__objects, __objects_reloaded)
