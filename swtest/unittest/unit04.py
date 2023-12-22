import unittest
import re

def is_valid_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("example@test.com"))
        self.assertTrue(is_valid_email("user.name@example.co.in"))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email("example.com"))
        self.assertFalse(is_valid_email("example@.com"))
        self.assertFalse(is_valid_email("@example.com"))
        self.assertFalse(is_valid_email("example@com"))

if __name__ == '__main__':
    unittest.main()