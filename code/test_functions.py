""" test_functions.py

    Functions used for creating tests
"""
from typing import Dict, Callable

from util import reset
from logger import get_logger

log = get_logger()


def test_digital_to_digital(test: Callable) -> str:
    """ Test a digital outout connected to a digital input line.
        This is a specialized test that's only meaningdful to self-r=test the baseboared

        args = {
            'set': Callable,    # output pin.set() function
            'read': Callable,   # input pin.read() function
        }
        returns: 'pass', 'fail', 'error'
    """
    test.test_dict['results'] = {}
    test.test_dict['results']['result'] = 'fail'
    params = test.test_dict['params']
    log.info("Running {:}".format(params['display']))
    pinout = getattr(test.pins, params['stimulus'])
    pinin = getattr(test.pins, params['response'])

    pinout.set(1)
    hi = pinin.read()
    pinout.set(0)
    lo = pinin.read()

    if hi == 1 and lo == 0:
        test.test_dict['results']['result'] = 'pass'
    return test.test_dict['results']['result']


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute test_primitives.py - EXITING")
