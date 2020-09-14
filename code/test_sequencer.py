""" test_sequencer.py

    This module runs a sequenc of tests.
    It uses test_runner to run each test.
    It uses test wrangler to assemble the sequence to run.
"""
from typing import Dict  # Callable

from util import fatal
# from test_runner import run_test
# import test_primitives as funcs


class test_sequence(object):
    """ Run a sequence of tests.
        Use as generator. Example:

        tests = test_sequence(test_specification_dictionary)
        while True:
            result = tests.next()
            if result is None:    # tests are complete
                break
    """

    def __init__(self, pin, test_set: Dict):
        self.pin = pin
        self.test_set = test_set

    def gen(self):
        """ test_name is the outer wrapper
            test_dicts contains the test, results, before... dictionaries
        """
        for test_name, test_dicts in self.test_set.tests.items():
            try:
                func = eval(test_dicts['test']['function'])
            except NameError:
                fatal("Unable to run test: {:}()".format(test_dicts['test']['function']))
            yield func, test_dicts
            # yield test_wrapper['test']

        # test = run_test(testM)
        # result = test.exec()
        # return result


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute test_sequencer.py - EXITING")
