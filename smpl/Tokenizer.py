"""
Tokenizer.py

Contains the implementation of the Tokenizer class.
"""

from FileReader import FileReader

class Tokenizer:
    """
    The Tokenizer is responsible for creating smpl tokens and sending it to 
    the smpl parser. \n
    
    It is implemented via a finite-state machine (FSM), with state transitions 
    done through the character stream of the FileReader. 
    """

    def __init__(self, file_name: str) -> None:
        """
        Initializes the Tokenizer class.

        :param file_name: Path to the input file.
        :type file_name: str
        """
        # Private
        self.__fileReader: FileReader = FileReader(file_name)
        self.__input_sym: str = self.__fileReader.get_next()

        # Public
        self.number: int = -1   # last number encountered
        self.id: int = -1       # last identifier encountered
        
    
    def __next(self) -> None:
        """
        Advances inputSym to the next character.
        """
        self.__input_sym = self.__fileReader.get_next()
    
    def get_next(self) -> int:
        """
        idk
        """
        pass

    def error(self, errorMsg: str) -> None:
        self.__fileReader.error(errorMsg)

    # Identifier Table methods
    def Id2String(id: int) -> str:
        pass

    def String2Id(name: str) -> int:
        pass
