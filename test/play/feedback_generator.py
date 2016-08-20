"""
Module testing the feedback generator
"""
from unittest import TestCase

from src.core.play.code import SecretCode, Attempt
from src.core.peg import CodePeg
from src.core.play.feedback_generator import FeedbackGenerator
from src.core.play.feedback import Feedback


class FeedbackGeneratorTest(TestCase):
    """
    Unit tests for the FeedbackGenerator
    """
    def setUp(self):
        """
        Setup each test to run with Green, Blue, Red, Green as the secret code.
        """
        SecretCode.instance().initialize(CodePeg.Green, CodePeg.Blue, CodePeg.Red, CodePeg.Green)

    def __validate(self, feedback, expected_black_count, expected_white_count):
        assert isinstance(feedback, Feedback), 'The feedback must be of type Feedback. Type passed: ' + str(type(feedback))
        assert isinstance(expected_black_count, int), 'The expected_black_count must be of type int. Type passed: ' + str(type(expected_black_count))
        assert isinstance(expected_white_count, int), 'The expected_white_count must be of type int. Type passed: ' + str(type(expected_white_count))
        if feedback.black_count != expected_black_count:
            self.fail('The amount of black peg(s) in the feedback is incorrect. Expected ' + str(expected_black_count) + ' and got: ' + str(feedback.black_count) + '.')
        if feedback.white_count != expected_white_count:
            self.fail('The amount of white peg(s) in the feedback is incorrect. Expected ' + str(expected_white_count) + ' and got: ' + str(feedback.white_count) + '.')

    def test_four_black(self):
        """
        Test an attempt with 4 black pegs as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Green, CodePeg.Blue, CodePeg.Red, CodePeg.Green))
        self.__validate(feedback, 4, 0)

    def test_three_black(self):
        """
        Test an attempt with 4 black pegs as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Green, CodePeg.Blue, CodePeg.Red, CodePeg.Black))
        self.__validate(feedback, 3, 0)

    def test_two_black_two_white(self):
        """
        Test an attempt with 2 black pegs and 2 white pegs as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Green, CodePeg.Blue, CodePeg.Green, CodePeg.Red))
        self.__validate(feedback, 2, 2)

    def test_two_black_one_white(self):
        """
        Test an attempt with 2 black pegs and 1 white peg as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Green, CodePeg.Blue, CodePeg.Black, CodePeg.Red))
        self.__validate(feedback, 2, 1)

    def test_two_black(self):
        """
        Test an attempt with 2 black pegs as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Green, CodePeg.Blue, CodePeg.Black, CodePeg.Black))
        self.__validate(feedback, 2, 0)

    def test_one_black_three_white(self):
        """
        Test an attempt with 1 black peg and 3 white pegs as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Green, CodePeg.Red, CodePeg.Green, CodePeg.Blue))
        self.__validate(feedback, 1, 3)

    def test_one_black_two_white(self):
        """
        Test an attempt with 1 black peg and 2 white pegs as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Green, CodePeg.Red, CodePeg.Green, CodePeg.Black))
        self.__validate(feedback, 1, 2)

    def test_one_black_one_white(self):
        """
        Test an attempt with 1 black peg and 1 white peg as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Green, CodePeg.Red, CodePeg.Black, CodePeg.Black))
        self.__validate(feedback, 1, 1)

    def test_one_black(self):
        """
        Test an attempt with 1 black peg as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Green, CodePeg.Black, CodePeg.Black, CodePeg.Black))
        self.__validate(feedback, 1, 0)

    def test_four_white(self):
        """
        Test an attempt with 4 white pegs as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Blue, CodePeg.Green, CodePeg.Green, CodePeg.Red))
        self.__validate(feedback, 0, 4)

    def test_three_white(self):
        """
        Test an attempt with 3 white pegs as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Black, CodePeg.Green, CodePeg.Blue, CodePeg.Red))
        self.__validate(feedback, 0, 3)

    def test_two_white(self):
        """
        Test an attempt with 2 white pegs as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Black, CodePeg.Black, CodePeg.Blue, CodePeg.Red))
        self.__validate(feedback, 0, 2)

    def test_one_white(self):
        """
        Test an attempt with 1 white peg as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Black, CodePeg.Black, CodePeg.Black, CodePeg.Red))
        self.__validate(feedback, 0, 1)

    def test_zero_black_zero_white(self):
        """
        Test an attempt with 0 black peg and 0 white peg as a feedback
        """
        feedback = FeedbackGenerator.generate_feedback(Attempt(CodePeg.Black, CodePeg.Black, CodePeg.Black, CodePeg.Black))
        self.__validate(feedback, 0, 0)
