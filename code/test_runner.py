""" test_runner.py

    This module runs a single test.
    It is typically called by test_sequencer
    It uses test_wrangler to assemble the test sequence.

    The basic structure of a test definition dictionary looks like this:
    test_name = {
        "before": {},
        "stimulus": {         # action[s] to initiate test
            "func": Callable  # function binding
            "args": <>        # int, float, Dict or None depending on func
        },
        "response": {},  # one or more responses to gather from stimulus
        "result": {},    # analyze, report and pass/fail callbacks from response
        "after": {},     # sero or more functions + args to run after test
    }
"""
# import sys
from typing import Dict  # Callable


class run_test(object):

    def __init__(self, test: Dict):
        # print("Connecting to g2core")
        self.test = test

    def exec(self):
        self.test['stimulus']['func'](self.test['stimulus']['args'])
        result = None
        return result


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute util.py - EXITING")
