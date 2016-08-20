"""
Main unit test routine
"""
from unittest import TestSuite, TextTestRunner, TestLoader

from test.play.feedback_generator import FeedbackGeneratorTest
from test.play.feedback import FeedbackTest
from test.play.secret_code import SecretCodeTest
from test.solver_engin.candidate_manager import CandidateManagerTest


# Loader and runner
loader = TestLoader()
test_runner = TextTestRunner(verbosity = 3)

# Adding the core test
core_test_suite = TestSuite()
core_test_suite.addTest(loader.loadTestsFromTestCase(FeedbackGeneratorTest))
core_test_suite.addTest(loader.loadTestsFromTestCase(FeedbackTest))
core_test_suite.addTest(loader.loadTestsFromTestCase(SecretCodeTest))
core_test_suite.addTest(loader.loadTestsFromTestCase(CandidateManagerTest))


# Running the tests
test_runner.run(core_test_suite)