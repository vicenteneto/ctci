import unittest

from chapter_1.check_permutation import check_permutation, check_permutation_without_sorting_string


class TestCheckPermutation(unittest.TestCase):
    TEST_DATA = [
        ('', '', True),
        (' ', ' ', True),
        ('asd', 'ads', True),
        ('asd', 'dsa', True),
        ('test', 'tests', False),
        ('test', 'tess', False),
    ]

    def test_check_permutation(self):
        for string_a, string_b, result in self.TEST_DATA:
            self.assertEqual(check_permutation(string_a, string_b), result)

    def test_check_permutation_without_sorting_string(self):
        for string_a, string_b, result in self.TEST_DATA:
            self.assertEqual(check_permutation_without_sorting_string(string_a, string_b), result)
