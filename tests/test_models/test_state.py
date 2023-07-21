#!/usr/bin/python3
"""
Unit tests for the State class
"""

import unittest
import pycodestyle
from models import state
from models.state import State
from models.base_model import BaseModel


class TestStateClass(unittest.TestCase):
    """Tests the State class"""

    def setUp(self):
        """Set up the test environment"""
        State.name = ""

    def test_pycodestyle(self):
        """Check state and test_state conform to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/state.py", "tests/test_models/test_state.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """Check module documentation"""
        self.assertTrue(len(state.__doc__) > 0)

    def test_class_doc(self):
        """Check class documentation"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_methods_doc(self):
        """Check methods documentation"""
        for method in dir(State):
            self.assertTrue(len(method.__doc__) > 0)

    def test_instance(self):
        """Check if object is a BaseModel instance"""
        self.assertTrue(isinstance(State(), BaseModel))

    def test_field_types(self):
        """Check if the attribute is the correct type"""
        self.assertTrue(isinstance(State().name, str))


if __name__ == "__main__":
    unittest.main()
