"""
Module that encapsulates the feedback generation
"""
from src.core.play.feedback import Feedback
from src.core.peg import CodePeg
from src.core.play.code import SecretCode, Attempt, Code


class FeedbackGenerator(object):
    """
    Class that encapsulates the process of feedback generation
    """
    @staticmethod
    def generate_feedback(attempt):
        """
        Method generating the appropriate feedback for a given attempt considering the secret code.

        Arguments:
            attempt (Attempt): The attempt on which the feedback is based

        Returns:
            Feedback: The feedback generated from the attempt and the secret code
        """
        assert isinstance(attempt, Code), 'The attempt must be of type Attempt. Type passed: ' + str(type(attempt))
        black_count = len([attempt_peg for attempt_peg, secret_peg in zip(attempt.code, SecretCode.instance().code) if attempt_peg == secret_peg])
        white_count = sum([min(attempt.code.count(color), SecretCode.instance().code.count(color)) for color in CodePeg]) - black_count
        return Feedback(black_count, white_count)

    @staticmethod
    def generate_feedback_for_given_code(attempt, code):
        """
        Method generating the appropriate feedback for a given attempt considering the secret code.

        Arguments:
            attempt (Attempt): The attempt on which the feedback is based
            code (list): The attempt that serve of reference for the feedback

        Returns:
            Feedback: The feedback generated from the attempt and the reference code
        """
        assert isinstance(attempt, Code), 'The attempt must be of type Attempt. Type passed: ' + str(type(attempt))
        black_count = len([attempt_peg for attempt_peg, secret_peg in zip(attempt.code, code) if attempt_peg == secret_peg])
        white_count = sum([min(attempt.code.count(color), code.count(color)) for color in CodePeg]) - black_count
        return Feedback(black_count, white_count)
