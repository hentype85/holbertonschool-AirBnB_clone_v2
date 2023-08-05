#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_cities_relationship(self):
        from models.city import City
        """Test if the relationship between State and City works."""
        new_state = State()
        new_city = City()
        new_state.cities.append(new_city)
        self.assertEqual(new_city.state, new_state)