"""
Main unit test routine
"""
from unittest import TestSuite, TextTestRunner, TestLoader

from test.feedback import FeedbackGeneratorTest


# Loader and runner
loader = TestLoader()
test_runner = TextTestRunner(verbosity = 3)

# Adding the core test
core_test_suite = TestSuite(loader.loadTestsFromTestCase(FeedbackGeneratorTest))

# Running the tests
test_runner.run(core_test_suite)