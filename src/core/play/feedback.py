"""
Module encapsulating the concept of feedback
"""
from src.core.peg import KeyPeg


class Feedback(object):
    """
    Module encapsulating the concept of feedback that a code maker respond

    Attributes:
        Attributes:
        black_count (int): The amount of black key pegs of the feedback
        white_count (int): The amount of white key pegs of the feedback
    """
    def __init__(self, black_count, white_count ):
        assert isinstance(black_count, int), 'The black_count is not of type int. Type passed: ' + str(type(black_count))
        assert isinstance(white_count, int), 'The white_count is not of type int. Type passed: ' + str(type(white_count))
        self.black_count, self.white_count = black_count, white_count
