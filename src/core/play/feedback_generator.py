"""
Module that encapsulates the feedback generation
"""
from src.core.play.feedback import Feedback
from src.core.peg import CodePeg
from src.core.play.code import SecretCode, Attempt


class FeedbackGenerator(object):
    """
    Class that encapsulates the process of feedback generation
    """
    @staticmethod
    def GenerateFeedback(attempt):
        assert isinstance(attempt, Attempt), 'The attempt must be of type Attempt. Type passed: ' + str(type(attempt))
        black_count = len([attempt_peg for attempt_peg, secret_peg in zip(attempt.code, SecretCode.instance().code) if attempt_peg == secret_peg])
        white_count = sum([min(attempt.code.count(color), SecretCode.instance().code.count(color)) for color in CodePeg]) - black_count
        return Feedback(black_count, white_count)
