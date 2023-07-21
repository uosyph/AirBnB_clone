#!/usr/bin/python3
"""
Unit tests for the BaseModel class
"""

import unittest
import os
import pycodestyle
from datetime import datetime
from time import sleep
from models import base_model
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Tests the BaseModel class"""

    def test_pycodestyle(self):
        """Check base_model and test_base_model conform to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/base_model.py", "tests/test_models/test_base_model.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_permissions(self):
        """Check if the file has the necessary permissions to be executed"""
        file = "models/base_model.py"
        self.assertTrue(os.access(file, os.F_OK))
        self.assertTrue(os.access(file, os.R_OK))
        self.assertTrue(os.access(file, os.W_OK))
        self.assertTrue(os.access(file, os.X_OK))

    def test_module_doc(self):
        """Check module documentation"""
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_doc(self):
        """Check class documentation"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_methods_doc(self):
        """Check methods documentation"""
        for method in dir(BaseModel):
            self.assertTrue(len(method.__doc__) > 0)

    def test_instance(self):
        """Check if object is a BaseModel instance"""
        self.assertTrue(isinstance(BaseModel(), BaseModel))

    def test_id_creation_and_uniqueness(self):
        """Check for id creation and uniqueness"""
        first_instance = BaseModel()
        second_instance = BaseModel()
        third_instance = BaseModel()
        self.assertTrue(first_instance.id != second_instance.id and
                        first_instance.id != third_instance.id)
        self.assertTrue(second_instance.id != first_instance.id and
                        second_instance.id != third_instance.id)
        self.assertTrue(third_instance.id != first_instance.id and
                        third_instance.id != second_instance.id)

    def test_id_type(self):
        """Check the type of id"""
        instance = BaseModel()
        self.assertTrue(isinstance(instance.id, str))

    def test_datetime_type(self):
        """Check the type of datetime"""
        instance = BaseModel()
        self.assertTrue(isinstance(instance.created_at, datetime))

    def test_string_output(self):
        """Check if output is string"""
        instance = BaseModel()
        self.assertEqual(instance.__str__(),
                         f"[{instance.__class__.__name__}]"
                         f" ({instance.id}) {str(instance.__dict__)}")


if __name__ == "__main__":
    unittest.main()