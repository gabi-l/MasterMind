"""
Module testing the secret code manipulation
"""
from unittest import TestCase

from src.core.play.code import SecretCode
from src.core.peg import CodePeg


class SecretCodeTest(TestCase):
    """
    Unit tests for the SecretCode
    """
    def test_secret_code_initialization(self):
        """
        Test the initialization of the secret code
        """
        SecretCode.instance().initialize(CodePeg.Green, CodePeg.Blue, CodePeg.Red, CodePeg.Yellow)
        if SecretCode.instance().code[0] != CodePeg.Green or \
           SecretCode.instance().code[1] != CodePeg.Blue or \
           SecretCode.instance().code[2] != CodePeg.Red or \
           SecretCode.instance().code[3] != CodePeg.Yellow:
            self.fail('The secret code did not initialize itself properly.')

    def test_secret_code_modification(self):
        """
        Test the modification of the secret code
        """
        SecretCode.instance().set(CodePeg.Yellow, CodePeg.Red, CodePeg.Blue, CodePeg.Green)
        if SecretCode.instance().code[0] != CodePeg.Yellow or \
           SecretCode.instance().code[1] != CodePeg.Red or \
           SecretCode.instance().code[2] != CodePeg.Blue  or \
           SecretCode.instance().code[3] != CodePeg.Green:
            self.fail('The secret code did not modified itself properly.')
