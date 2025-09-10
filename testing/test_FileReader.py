import unittest
from unittest.mock import MagicMock, patch

from smpl.FileReader import FileReader

class TestFileReader(unittest.TestCase):

    @patch('builtins.open')
    def test_get_next_normal(self, mock_open):
        """
        Tests reading a normal string of chars. 
        """
        # creating the mock file object
        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_file.__iter__.return_value = iter("Hello")

        # mock file read
        mock_file.read.side_effect = list("Hello") + ['', '']
        mock_open.return_value = mock_file

        reader = FileReader('test.txt')

        # actually testing get_next
        self.assertEqual(reader.get_next(), 'H')
        self.assertEqual(reader.get_next(), 'e')
        self.assertEqual(reader.get_next(), 'l')
        self.assertEqual(reader.get_next(), 'l')
        self.assertEqual(reader.get_next(), 'o')
        self.assertEqual(reader.get_next(), FileReader.EOF)
        self.assertEqual(reader.get_next(), FileReader.EOF)


    @patch('builtins.open')
    def test_get_next_empty(self, mock_open):
        """
        Tests reading from empty file. 
        """
        # creating the mock file object
        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file

        # read (nothing this time)
        mock_file.read.return_value = ''
        mock_open.return_value = mock_file

        reader = FileReader('test.txt')

        self.assertEqual(reader.get_next(), FileReader.EOF)
        self.assertEqual(reader.get_next(), FileReader.EOF)

    @patch('builtins.print')
    def test_error(self, mock_print):
        """
        Tests error function and flagging. 
        """
        reader = FileReader('test.txt')

        err_msg = "sample error"
        reader.error(err_msg)

        self.assertTrue(reader.is_error)
        mock_print.assert_called_once_with(err_msg)

    @patch('builtins.print')
    def test_get_next_error(self, mock_print):
        """
        Tests that get_next only returns error characters. 
        """
        reader = FileReader('test.txt')
        reader.error('sample error')
        
        self.assertEqual(reader.get_next(), FileReader.Error)
        self.assertEqual(reader.get_next(), FileReader.Error)
        self.assertEqual(reader.get_next(), FileReader.Error)

if __name__ == "__main__":
    unittest.main()