import unittest

from chapter_1.is_unique import is_unique, is_unique_without_data_structure
from chapter_1.is_unique import is_unique_without_data_structure_sorting_string


class TestIsUnique(unittest.TestCase):
    TEST_DATA = [
        ('', True),
        (' ', True),
        ('  ', False),
        ('a', True),
        ('aa', False),
        ('ab', True),
        ('ab ', True),
        ('test', False)
    ]

    def test_is_unique_with_character_set_size(self):
        self.assertFalse(is_unique('qwerty', 5))
        self.assertTrue(is_unique('qwerty', 6))

    def test_is_unique(self):
        for string, result in self.TEST_DATA:
            self.assertEqual(is_unique(string), result)

    def test_is_unique_without_data_structure(self):
        for string, result in self.TEST_DATA:
            self.assertEqual(is_unique_without_data_structure(string), result)

    def test_is_unique_without_data_structure_sorting_string(self):
        for string, result in self.TEST_DATA:
            self.assertEqual(is_unique_without_data_structure_sorting_string(string), result)
