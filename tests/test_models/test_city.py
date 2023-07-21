#!/usr/bin/python3
"""
Unit tests for the City class
"""

import unittest
import pycodestyle
from models import city
from models.city import City
from models.base_model import BaseModel


class TestCityClass(unittest.TestCase):
    """Tests the City class"""

    def setUp(self):
        """Set up the test environment"""
        City.name = ""
        City.state_id = ""

    def test_pycodestyle(self):
        """Check city and test_city conform to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/city.py", "tests/test_models/test_city.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """Check module documentation"""
        self.assertTrue(len(city.__doc__) > 0)

    def test_class_doc(self):
        """Check class documentation"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_methods_doc(self):
        """Check methods documentation"""
        for method in dir(City):
            self.assertTrue(len(method.__doc__) > 0)

    def test_instance(self):
        """Check if object is a BaseModel instance"""
        self.assertTrue(isinstance(City(), BaseModel))

    def test_field_types(self):
        """Check if the attributes are the correct type"""
        self.assertTrue(isinstance(City().state_id, str))
        self.assertTrue(isinstance(City().name, str))


if __name__ == "__main__":
    unittest.main()
