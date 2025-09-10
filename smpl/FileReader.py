"""
FileReader.py

Contains the implementation of the FileReader class. 
"""

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
        self.__file_name: str = file_name
        self.__is_error: bool = False
        try:
            self.__char_generator: Generator[str, None, None] = self.__get_next_util()
        except Exception as e:
            self.error(str(e))
    
    def error(self, err_msg: str) -> None:
        """
        Prints the error message. 

        :param err_msg: Error message to be shown.
        :type err_msg: str
        """
        self.__is_error = True
        print(err_msg)

    def get_next(self) -> str | int:
        """
        Returns the next character in sequence from the file. \n

        :return: Next character in the file.
        :rtype: str
        """
        if self.__is_error: 
            return FileReader.Error

        try:
            ch: str = next(self.__char_generator)
            return ch
        except StopIteration:
            return FileReader.EOF
            
    def __get_next_util(self) -> Generator[str, None, None]:
        """
        Utility function/generator for the next character in
        the file. Sends '' if end of file. 

        :return: A generator for the next character in sequence
        :rtype: Generator 
        """
        try:
            with open(self.__file_name, 'r') as file:
                while True:
                    ch: str | None = file.read(1)
                    if not ch:
                        break
                    yield ch
        except Exception as e:
            self.error(str(e))