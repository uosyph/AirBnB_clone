#!/usr/bin/python3
"""
Unit tests for the Review class
"""

import unittest
import pycodestyle
from models import review
from models.review import Review
from models.base_model import BaseModel


class TestReviewClass(unittest.TestCase):
    """Tests the Review class"""

    def test_pycodestyle(self):
        """Check review and test_review conform to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/review.py", "tests/test_models/test_review.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """Check module documentation"""
        self.assertTrue(len(review.__doc__) > 0)

    def test_class_doc(self):
        """Check class documentation"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_methods_doc(self):
        """Check methods documentation"""
        for method in dir(Review):
            self.assertTrue(len(method.__doc__) > 0)

    def test_instance(self):
        """Check if object is a BaseModel instance"""
        self.assertTrue(isinstance(Review(), BaseModel))

    def test_field_types(self):
        """Check if the attributes are the correct type"""
        self.assertTrue(isinstance(Review().place_id, str))
        self.assertTrue(isinstance(Review().user_id, str))
        self.assertTrue(isinstance(Review().text, str))


if __name__ == "__main__":
    unittest.main()
