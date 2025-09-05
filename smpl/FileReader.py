"""
FileReader.py

Contains the implementation of the FileReader class. 
"""

from Exceptions import CompileError
from typing import Generator

class FileReader:
    """
    The FileReader is in charge of reading the input to the smpl compiler. \n
    
    Input is given as a input text file. Characters are parsed one-by-one 
    until an error or EOF is reached. 
    """
    Error = 0   # enum type for error
    EOF = 255   # enum type for end of file

    def __init__(self, file_name: str) -> None:
        """
        Initializes the FileReader class.

        :param file_name: Path to the input file.
        :type file_name: str
        """
        self.file_name: str = file_name
        self.is_error: bool = False
    
    def error(self, err_msg: str) -> None:
        """
        Raises an error with the given error message.

        :param err_msg: Error message to be shown.
        :type err_msg: str
        """
        self.is_error = True
        raise CompileError(err_msg)

    def get_next(self) -> str | int:
        """
        Returns the next character in sequence from the file. \n

        :return: Next character in the file.
        :rtype: str
        """
        if self.is_error: 
            return FileReader.Error

        ch: str = self.__get_next_util()
        if ch == '':
            return FileReader.EOF
        
        return ch
            
    def __get_next_util(self) -> Generator[str, None, None]:
        """
        Utility function/generator for the next character in
        the file. Sends '' if end of file. 

        :return: A generator for the next character in sequence
        :rtype: Generator 
        """
        try:
            with open(self.file_name, 'r') as file:
                ch: str | None = file.read(1)
                while ch:
                    ch = file.read(1)
                    yield ch
        except Exception as e:
            self.error(e)