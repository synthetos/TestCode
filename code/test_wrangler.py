""" test_wrangler.py

    This module collects tests and returns a test_set dictionary.
"""
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
    print("Tried to execute util.py - EXITING")
