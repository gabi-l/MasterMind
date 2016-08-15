"""
Module that encapsulate the concept of pin
"""
from enum import Enum


class Peg(Enum):
    """
    Class that encapsulate the concept of peg
    """
    pass


class CodePeg(Peg):
    """
    Class that encapsulate the concept of code pegs
    """
    Green = 0
    Blue = 1
    Red = 2
    Yellow = 3
    Black = 4
    White = 5


class KeyPeg(Peg):
    """
    Class that encapsulate the concept of key pegs
    """
    Black = 0
    White = 1
