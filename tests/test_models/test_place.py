#!/usr/bin/python3
"""
Unit tests for the Place class
"""

import unittest
import pycodestyle
from models import place
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """Tests the Place class"""

    def setUp(self):
        """Set up the test environment"""
        Place.city_id = ""
        Place.user_id = ""
        Place.name = ""
        Place.description = ""
        Place.number_rooms = 0
        Place.number_bathrooms = 0
        Place.max_guest = 0
        Place.price_by_night = 0
        Place.latitude = 0.0
        Place.longitude = 0.0
        Place.amenity_ids = []

    def test_pycodestyle(self):
        """Check place and test_place conform to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/place.py", "tests/test_models/test_place.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """Check module documentation"""
        self.assertTrue(len(place.__doc__) > 0)

    def test_class_doc(self):
        """Check class documentation"""
        self.assertTrue(len(Place.__doc__) > 0)

    def test_methods_doc(self):
        """Check methods documentation"""
        for method in dir(Place):
            self.assertTrue(len(method.__doc__) > 0)

    def test_instance(self):
        """Check if object is a BaseModel instance"""
        self.assertTrue(isinstance(Place(), BaseModel))

    def test_field_types(self):
        """Check if the attributes are the correct type"""
        self.assertTrue(isinstance(Place().city_id, str))
        self.assertTrue(isinstance(Place().user_id, str))
        self.assertTrue(isinstance(Place().name, str))
        self.assertTrue(isinstance(Place().description, str))
        self.assertTrue(isinstance(Place().number_rooms, int))
        self.assertTrue(isinstance(Place().number_bathrooms, int))
        self.assertTrue(isinstance(Place().max_guest, int))
        self.assertTrue(isinstance(Place().price_by_night, int))
        self.assertTrue(isinstance(Place().latitude, float))
        self.assertTrue(isinstance(Place().longitude, float))
        self.assertTrue(isinstance(Place().amenity_ids, list))


if __name__ == "__main__":
    unittest.main()
