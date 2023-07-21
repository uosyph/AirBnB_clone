#!/usr/bin/python3
"""
Unit tests for the Amenity class
"""

import unittest
import os
import pycodestyle
from models import amenity
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityClass(unittest.TestCase):
    """Tests the Amenity class"""

    def test_pycodestyle(self):
        """Check amenity and test_amenity conform to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/amenity.py", "tests/test_models/test_amenity.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """Check module documentation"""
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_class_doc(self):
        """Check class documentation"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_methods_doc(self):
        """Check methods documentation"""
        for method in dir(Amenity):
            self.assertTrue(len(method.__doc__) > 0)

    def test_instance(self):
        """Check if object is a BaseModel instance"""
        self.assertTrue(isinstance(Amenity(), BaseModel))

    def test_field_types(self):
        """Check if the attribute is the correct type"""
        self.assertTrue(isinstance(Amenity().name, str))


if __name__ == "__main__":
    unittest.main()
