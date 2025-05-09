"""
FileReader.py

Contains the implementation of the FileReader class. 
"""

class FileReader:
    """
    The FileReader is in charge of reading the input to the smpl compiler. \n
    
    Input is given as a input text file. Characters are parsed one-by-one 
    until an error or EOF is reached. 
    """

    def __init__(self, fileName: str) -> None:
        """
        Initializes the FileReader class.

        :param fileName: Path to the input file.
        :type fileName: str
        """
        self.file = None
        with open(fileName, 'r') as file:
            self.file = file
    
    def error(self, errMsg: str) -> None:
        """
        

        """
        pass

    def get_next(self) -> str:
        """
        Returns the next character in sequence from the file.

        :return: Next character in the file.
        :rtype: str
        """
        if self.file is None:
            self.error('no file idk')
        

        
