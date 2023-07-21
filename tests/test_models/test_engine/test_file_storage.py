#!/usr/bin/python3
"""
Unit tests for the FileStorage class
"""

import unittest
import os
import pycodestyle
from models import storage
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage class"""

    def test_pycodestyle(self):
        """Check file_storage and test_file_storage conform to pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files([
            "models/engine/file_storage.py",
            "tests/test_models/test_engine/test_file_storage.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """Check module documentation"""
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_class_doc(self):
        """Check class documentation"""
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_methods_doc(self):
        """Check methods documentation"""
        for method in dir(FileStorage):
            self.assertTrue(len(method.__doc__) > 0)

    def test_instance(self):
        """Check if object is a FileStorage instance"""
        self.assertTrue(isinstance(storage, FileStorage))

    def test_all_method(self):
        """Check if the all() method returns the correct type"""
        self.assertTrue(isinstance(FileStorage().all(), dict))

    def test_reload_method(self):
        """Check the reload() method"""
        obj = FileStorage()
        obj.new(BaseModel())
        obj.save()

        first_dict = obj.all()
        os.remove("test.json")
        obj.reload()
        second_dict = obj.all()
        self.assertTrue(first_dict == second_dict)


if __name__ == "__main__":
    unittest.main()
