import unittest

def divide(a, b):
    if b == 0:
        raise ValueError("분모는 0이 될 수 없습니다.")
    return a / b

class TestDivideFunction(unittest.TestCase):
    def test_divide_normal(self):
        self.assertEqual(divide(4, 2), 2)
        self.assertEqual(divide(-6, 3), -2)

    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()