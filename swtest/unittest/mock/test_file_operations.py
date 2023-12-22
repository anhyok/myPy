# test_file_operations.py

import unittest
from unittest.mock import mock_open, patch
from file_operations import write_to_file

class TestFileOperations(unittest.TestCase):
    @patch("file_operations.open", new_callable=mock_open, read_data="data")
    def test_write_to_file(self, mock_file):
        # 함수를 호출합니다.
        write_to_file("test.txt", "Hello, World!")

        # open이 호출되었는지 확인합니다.
        mock_file.assert_called_with("test.txt", "w")

        # 파일에 쓰기가 올반게 되었는지 확인합니다.
        mock_file().write.assert_called_with("Hello, World!")

if __name__ == '__main__':
    unittest.main()
