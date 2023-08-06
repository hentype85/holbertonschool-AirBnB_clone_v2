#!/usr/bin/python3
""" Module for testing database storage"""
import unittest
from models import getenv
from models import storage
from models.engine.db_storage import DBStorage

class test_DataBaseStorage(unittest.TestCase):
    """test Database storage"""

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "skip")
    def test_class(self):
        self.storage = DBStorage()
