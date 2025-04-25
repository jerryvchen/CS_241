from main import WU2_Interpreter

import unittest
from unittest.mock import patch
from io import StringIO

class Test_W2_Interpreter(unittest.TestCase):
    # given test case on hw description
    basic_str = 'computation var i <- 2 * 3; var abracadabra <- 7; (((abracadabra * i))); i - 5 - 1.'
    @patch('builtins.input', return_value=basic_str)
    @patch('sys.stdout', new_callable=StringIO)
    def test_basic(self, mock_stdout, mock_input):
        WU2_Interpreter()
        self.assertEqual(mock_stdout.getvalue(), "42\n0\n")

    # test var named variable (same prefix)
    prefix_str = 'computation var variable <- 1 + 82; ((variable * 3)); variable - 62.'
    @patch('builtins.input', return_value=prefix_str)
    @patch('sys.stdout', new_callable=StringIO)
    def test_prefix(self, mock_stdout, mock_input):
        WU2_Interpreter()
        self.assertEqual(mock_stdout.getvalue(), "249\n21\n")

    # test on WU1 test case (no identifers, superflous whitespace)
    wu1_str = 'computation 1 +2 *(3+4) ; 7 * 6 .'
    @patch('builtins.input', return_value=wu1_str)
    @patch('sys.stdout', new_callable=StringIO)
    def test_wu1(self, mock_stdout, mock_input):
        WU2_Interpreter()
        self.assertEqual(mock_stdout.getvalue(), "15\n42\n")
        
if __name__ == '__main__':
    unittest.main()