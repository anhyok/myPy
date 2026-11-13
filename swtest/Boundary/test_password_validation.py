# test_password_validation.py

import unittest
from password_validation import validpass

class TestPasswordValidation(unittest.TestCase):
    def test_password_length_7(self):
        self.assertFalse(validpass("1234567"))  # 7자

    def test_password_length_8(self):
        self.assertTrue(validpass("12345678"))  # 8자

    def test_password_length_20(self):
        self.assertTrue(validpass("12345678901234567890"))  # 20자

    def test_password_length_21(self):
        self.assertFalse(validpass("123456789012345678901"))  # 21자

if __name__ == '__main__':
    unittest.main()