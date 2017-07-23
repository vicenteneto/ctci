import unittest

from chapter_1.check_permutation import check_permutation


class TestCheckPermutation(unittest.TestCase):
    TEST_DATA = [
        ('', '', True),
        (' ', ' ', True),
        ('asd', 'ads', True),
        ('asd', 'dsa', True),
        ('test', 'tests', False)
    ]

    def test_check_permutation(self):
        for string_a, string_b, result in self.TEST_DATA:
            self.assertEqual(check_permutation(string_a, string_b), result)
