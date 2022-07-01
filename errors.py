"""
Errors implementation
"""

class InputIsNumberError(Exception):
    """
    Error for when the input is a number
    """
    pass

class LetterAlreadyInsertedError(Exception):
    """
    Error for when the selected letter had already been inserted
    """
    pass

class WrongInputError(Exception):
    """
    Error for when the input is not in the word
    """
    pass

class WordAlreadyTriedError(Exception):
    """
    Error for when the attempted word had already been tried
    """
    pass

class InvalidOptionError(Exception):
    """
    Error for when the selected option is different from Y or N
    """
    pass
