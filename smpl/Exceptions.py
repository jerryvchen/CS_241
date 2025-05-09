"""
Exceptions.py

Contains the implementation of any Exception class in the smpl compiler.
"""

class CompileError(Exception):
    """
    An exception that is raised whenever an error is encountered during 
    the compilation of a smpl program.
    """
    def __init__(self, err_msg: str) -> None:
        """
        Initializes the CompileError class.

        :param err_msg: Error message to be printed.
        :type err_msg: str
        """
        super().__init__(err_msg)