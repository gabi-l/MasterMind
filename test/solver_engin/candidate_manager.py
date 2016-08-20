"""
Module testing the candidate manager manipulations
"""
from unittest import TestCase

from src.core.solver_engine.candidate_manager import CandidateManager


class CandidateManagerTest(TestCase):
    """
    Unit tests for the CandidateManager
    """
    @staticmethod
    def __is_duplicate_present_in_list(elements):
        seen = set()
        for element in elements:
            if element in seen:
                return True
            seen.add(element)
        return False

    def test_secret_code_initialization(self):
        """
        Test the initialization of the candidate manager (non exhaustive test)
        """
        if len(CandidateManager.instance()._get_all_possible_code()) != pow(6,4):
            self.fail('The candidate manager did not initialize properly. It does not contain 1296 elements.')
        if self.__is_duplicate_present_in_list(CandidateManager.instance()._get_all_possible_code()):
            self.fail('The canadidate manager did not initialize properly. It contains duplicate values.')
        CandidateManager.instance().initialize()
        if len([candidate_a for candidate_a, candidate_b in zip(CandidateManager.instance()._get_current_candidates_left(), CandidateManager.instance()._get_all_possible_code()) if candidate_a == candidate_b]) != pow(6,4):
            self.fail('The candidate manager did not initialize properly. Initially the current candidates left are not equal to all the possible codes')