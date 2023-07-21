#!/usr/bin/python3
"""
Unit tests for the User class
"""

import unittest
import pycodestyle
from models import user
from models.user import User
from models.base_model import BaseModel


class TestUserClass(unittest.TestCase):
    """Tests the User class"""

    def setUp(self):
        """Set up the test environment"""
        User.email = ""
        User.password = ""
        User.first_name = ""
        User.last_name = ""

    def test_pycodestyle(self):
        """Check user and test_user conform to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(["models/user.py",
                                    "tests/test_models/test_user.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """Check module documentation"""
        self.assertTrue(len(user.__doc__) > 0)

    def test_class_doc(self):
        """Check class documentation"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_methods_doc(self):
        """Check methods documentation"""
        for method in dir(User):
            self.assertTrue(len(method.__doc__) > 0)

    def test_instance(self):
        """Check if object is a BaseModel instance"""
        self.assertTrue(isinstance(User(), BaseModel))

    def test_field_types(self):
        """Check if the attributes are the correct type"""
        self.assertTrue(isinstance(User().email, str))
        self.assertTrue(isinstance(User().password, str))
        self.assertTrue(isinstance(User().first_name, str))
        self.assertTrue(isinstance(User().last_name, str))


if __name__ == "__main__":
    unittest.main()
