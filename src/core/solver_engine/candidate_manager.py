"""
Module encapsulating the candidates
"""
from itertools import product
from copy import deepcopy

from src.core.peg import CodePeg
from src.core.play.code import Code


def tuple_to_code(code_tuple):
    return Code(code_tuple[0], code_tuple[1], code_tuple[2], code_tuple[3])


class CandidateManager(object):
    """
    Class managing the possible code candidates
    """
    __instance = None

    def __init__(self):
        self.__all_possible_code = [tuple(p) for p in product(CodePeg, repeat=4)]
        for index in range(0, len(self.__all_possible_code)):
            self.__all_possible_code[index] = tuple_to_code(self.__all_possible_code[index])
        self.__current_candidates_left = list()

    @classmethod
    def instance(cls):
        """
        Method used to access the CandidateManager instance
        """
        if cls.__instance is None:
            cls.__instance = CandidateManager()
        return cls.__instance

    def initialize(self):
        """
        Method initializing the CandidateManager
        """
        self.__current_candidates_left = deepcopy(self.__all_possible_code)

    def _get_all_possible_code(self):
        """
        Accessor method returning all the possible candidates

        Returns:
            list: All the possible combination of code

        Note:
            Caller MUST not modify the content of the returned object. The raw instance is return to save a deepcopy.
        """
        return self.__all_possible_code

    def _get_current_candidates_left(self):
        """
        Accessor method returning the current candidate left in the run

        Returns:
            list: The combination of code that are still possible

        Note:
            Caller is responsible to maintain the list in a logical state. The raw instance is return to save a deepcopy.
        """
        return self.__current_candidates_left
