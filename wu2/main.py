##### Warm-Up 2 (wu2) Interpreter #####
from enum import Enum

class WU2_Word(Enum):
    """
    The Reserved Words Table for the WU2_Interpreter.
    """
    
    COMPUTATION = 0
    VAR = 1
    LARROW = 2 # <- | ex: var a <- 2

class WU2_Tokenizer:
    """
    The Tokenizer for the WU2_Interpreter.

    Specifically parses:
    - identifiers
    - numbers
    - special symbols
    """
    def __init__(self, input_str):
        """
        Initializes the Tokenizer
        """
        self.in_str = reversed([ch for ch in input_str])
        self.curr = None
        self.next = None

        # finite state machine
        self.fsm = {
            0: {1, 2, 3},

        }
        # 0: start state
        # 1: 
        self.state = 0
        self.val = None
    
    def _get_next_ch(self):
        pass

    def get_next(self) -> int:
        """
        Returns the next token.

        """
        return 0


class WU2_Interpreter:
    def __init__(self):
        input_str = input()
        self.tokenizer = WU2_Tokenizer(input_str)
        
        self.sym = None

    def factor(self):
        pass

    def term(self):
        pass

    def expression(self):
        pass

    def computation(self):
        pass

