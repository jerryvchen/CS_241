"""
Parser.py

Contains the implementation of the Parser class. 
"""

from Tokenizer import Tokenizer

class Parser:
    def __init__(self, fileName: str) -> None:
        # Private 
        self.__tokenizer = Tokenizer(fileName)
        self.__input_sym: int = -1      # current token on the input

        ### Parser
        self.__next()   # cache first token
        
    
    def __next(self) -> None:
        """
        Advances inputSym to the next token.
        """
        self.__input_sym = self.__tokenizer.get_next()

    def CheckFor(self, token: int) -> None:
        if self.__input_sym == token:
            self.__next()
        else:
            self.__tokenizer.error("SyntaxErr")
    
