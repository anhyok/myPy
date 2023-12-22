# test_user_category.py

import unittest
from user_category import categorize_user

class TestUserCategory(unittest.TestCase):
    def test_child_category(self):
        self.assertEqual(categorize_user(10), "어린이")

    def test_teen_category(self):
        self.assertEqual(categorize_user(15), "청소년")

    def test_adult_category(self):
        self.assertEqual(categorize_user(20), "성인")

    def test_invalid_age(self):
        self.assertEqual(categorize_user(-1), "유효하지 않은 나이")

if __name__ == '__main__':
    unittest.main()
