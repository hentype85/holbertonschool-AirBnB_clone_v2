#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from datetime import datetime

class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.password), str)
    
    def test_attributes(self):
        """ """
        new = User(email="a", password="a")
        self.assertEqual(str, type(new.id))
        self.assertEqual(datetime, type(new.created_at))
        self.assertEqual(datetime, type(new.updated_at))
        self.assertTrue(hasattr(new, "__tablename__"))
        self.assertTrue(hasattr(new, "email"))
        self.assertTrue(hasattr(new, "password"))
        self.assertTrue(hasattr(new, "first_name"))
        self.assertTrue(hasattr(new, "last_name"))
        self.assertTrue(hasattr(new, "places"))
        self.assertTrue(hasattr(new, "reviews"))
