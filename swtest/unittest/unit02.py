import unittest

def reverse_string(s):
    return s[::-1]

class TestReverseStringFunction(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string(" "), " ")
        self.assertEqual(reverse_string(" a "), " a ")

if __name__ == '__main__':
    unittest.main()