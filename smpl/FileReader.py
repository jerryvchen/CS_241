"""
FileReader.py

Contains the implementation of the FileReader class. 
"""

from Exceptions import CompileError

class FileReader:
    """
    The FileReader is in charge of reading the input to the smpl compiler. \n
    
    Input is given as a input text file. Characters are parsed one-by-one 
    until an error or EOF is reached. 
    """

    def __init__(self, file_name: str) -> None:
        """
        Initializes the FileReader class.

        :param file_name: Path to the input file.
        :type file_name: str
        """
        self.file_name: str = file_name
    
    def error(self, err_msg: str) -> None:
        """
        Raises an error with the given error message.

        :param err_msg: Error message to be shown.
        :type err_msg: str
        """
        raise CompileError(err_msg)

    def get_next(self) -> str:
        """
        Returns the next character in sequence from the file.

        :return: Next character in the file.
        :rtype: str
        """
        with open(self.file_name, 'r') as file:
            ch: str | None = file.read(1)
            while ch:
                ch = file.read(1)
                yield ch
            
    
