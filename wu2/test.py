from main import WU2_Interpreter

import unittest
from unittest.mock import patch
from io import StringIO

class Test_W2_Interpreter(unittest.TestCase):
    test1_str = 'computation var i <- 2 * 3; var abracadabra <- 7; (((abracadabra * i))); i - 5 - 1.'

    @patch('builtins.input', return_value=test1_str)
    def test_1(self, mocked_input):
        WU2_Interpreter()

if __name__ == '__main__':
    unittest.main()