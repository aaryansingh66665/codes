import unittest
from unittest.mock import mock_open, patch  # Assuming the file is named _2.py to avoid conflict


class TestFileOperations(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="0123456789abcdef")
    def test_read_partial(self, mock_file):
        _2.f = open("test.txt", "r")
        data = _2.f.read(10)
        self.assertEqual(data, "0123456789")
        _2.f.close()

    @patch("builtins.open", new_callable=mock_open, read_data="First line\nSecond line\n")
    def test_readline(self, mock_file):
        _2.f = open("test.txt", "r")
        data1 = _2.f.readline()
        self.assertEqual(data1, "First line\n")
        _2.f.close()

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_read_empty_file(self, mock_file):
        _2.f = open("test.txt", "r")
        data = _2.f.read(10)
        self.assertEqual(data, "")
        _2.f.close()

    @patch("builtins.open", new_callable=mock_open, read_data="SingleLine")
    def test_readline_single_line(self, mock_file):
        _2.f = open("test.txt", "r")
        data1 = _2.f.readline()
        self.assertEqual(data1, "SingleLine")
        _2.f.close()
