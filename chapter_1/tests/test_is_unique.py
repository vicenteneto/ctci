import unittest

from chapter_1.is_unique import is_unique, is_unique_without_data_structure


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

    def test_is_unique(self):
        for string, result in self.TEST_DATA:
            self.assertEqual(is_unique(string), result)

    def test_is_unique_without_data_structure(self):
        for string, result in self.TEST_DATA:
            self.assertEqual(is_unique_without_data_structure(string), result)
