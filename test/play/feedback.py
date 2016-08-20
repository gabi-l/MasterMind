"""
Module testing the feedback manipulation
"""
from unittest import TestCase

from src.core.play.feedback import Feedback


class FeedbackTest(TestCase):
    """
    Unit tests for the Feedback
    """
    def test_feedback_not_equal_operator_true(self):
        """
        Test the feedback logical not equal overload with true return
        """
        if Feedback(0,0) != Feedback(0,0):
            self.fail('The feedback logical not equal operator is not acting properly.')

    def test_feedback_not_equal_operator_false_1(self):
        """
        First test of the feedback logical not equal overload with false return
        """
        if not Feedback(1, 0) != Feedback(0, 0):
            self.fail('The feedback logical not equal operator is not acting properly.')

    def test_feedback_not_equal_operator_false_2(self):
        """
        Second test of the feedback logical not equal overload with false return
        """
        if not Feedback(0, 0) != Feedback(0, 1):
            self.fail('The feedback logical not equal operator is not acting properly.')

    def test_feedback_not_equal_operator_false_3(self):
        """
        Third test of the feedback logical not equal overload with false return
        """
        if not Feedback(1, 0) != Feedback(0, 1):
            self.fail('The feedback logical not equal operator is not acting properly.')
