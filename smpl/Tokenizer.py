"""
Tokenizer.py

Contains the implementation of the Tokenizer class.
"""

from FileReader import FileReader

class Tokenizer:
    """
    pass
    """

    def __init__(self, fileName: str) -> None:
        """
        idk
        """
        # Private
        self.__fileReader: FileReader = FileReader(fileName)
        self.__input_sym: str = ''

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
