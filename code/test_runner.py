""" test_runner.py

    This module runs a single test.
    It is typically called by test_sequencer
    It uses test_wrangler to assemble the test sequence.

    The basic structure of a test definition dictionary looks like this:

    test_name = {
        'display': 'String to display'  (may be absent)
        'before': {},                   (may be absent)
        'stimulus': {         # action[s] to initiate test
            'func': Callable  # stimulus function (binding)
            'args': Any       # int, float, Dict or None depending on func
        },
        'response': {         # action[s] to initiate test
            'func': Callable  # response function (binding)
            'args': Any       # int, float, Dict or None depending on func
        },
        'result': {},         # analyze, report and pass/fail callbacks from response
        'after': {},          # zero or more functions to run after test (may be absent)
    }

    ToDo: 
    - Make before, stimulus, response and after optionally accept an array of Dicts
"""
# import sys
from typing import Dict  # Callable


class run_test(object):
    """ Run a test and evaluate the reults
    """

    def __init__(self, test: Dict):
        # print("Connecting to g2core")
        self.test = test
        self.results = []

    def exec(self):
        if not isinstance(self.test['stimulus'], list):
            self.test['stimulus'] = [self.test['stimulus']]
        if not isinstance(self.test['response'], list):
            self.test['response'] = [self.test['response']]

        for i in range(len(self.test['stimulus'])):
            self.test['stimulus'][i]['func'](self.test['stimulus'][i]['args'])
            result = self.test['response'][i]['func'](self.test['response'][i]['args'])
            self.results.append(result)

        # for stim in self.test['stimulus']:
        #     self.test['stimulus']['func'](self.test['stimulus']['args'])
        #     result = self.test['response']['func'](self.test['response']['args'])
        #     self.results = result
        return result


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute test_runner.py - EXITING")
