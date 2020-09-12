""" test_sequencer.py

    This module runs a sequenc of tests.
    It uses test_runner to run each test.
    It uses test wrangler to assemble the sequence to run.
"""
from typing import Dict  # Callable

from test_runner import run_test


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
        # print("Connecting to g2core")
        self.pin = pin
        self.test_set = test_set

    def next(self):

        testN = {
            'before': {},
            'stimulus': {
                'func': self.pin.dout3.set,
                'args': 1
            },
            'response': {},
            'result': {},
            'after': {},
        }
        test = run_test(testN)
        result = test.exec()
        return result


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute util.py - EXITING")
