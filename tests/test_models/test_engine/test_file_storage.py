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

    def setUp(self):
        """Set up the test environment"""
        with open("test.json", "w"):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down the test environment"""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

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

    def test_new_method(self):
        """Check the new() method"""
        instance = BaseModel()
        obj = FileStorage()
        obj.new(instance)
        self.assertTrue(
            f"{type(instance).__name__}.{instance.id}" in obj.all())

    def test_save_method(self):
        """Check the save() method"""
        obj = FileStorage()
        obj.new(BaseModel())
        first_dict = obj.all()
        obj.save()
        obj.reload()
        second_dict = obj.all()

        for key in first_dict:
            first_key = key
        for key in second_dict:
            second_key = key
        self.assertEqual(first_dict[first_key].to_dict(),
                         second_dict[second_key].to_dict())

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
