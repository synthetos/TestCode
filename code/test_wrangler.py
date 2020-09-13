""" test_wrangler.py

    This module collects tests and returns a test_set dictionary.

    The wrangler's job is to load abstract definitions for the tests
    and resolve them into executable functions that the sequencer / runner
    can execute directly.

    As such - it needs to know the functions for all these tests,
    so as test types are added they need to be added to the loader.

    To add a new test type include and document it in the loader
    and add it to the function_map in the __init__
"""
from typing import Dict, Callable

from test_primitives import test_digital_to_digital     # self-test of the tester board itself
from util import fatal
from logger import get_logger

log = get_logger()


# Temporary definition for a test before I get the JSON load functions going
test_spec = {
    'test_pin3': {
        'display': "Test pin 3",
        'function': 'digital_self_test',
        'stimulus': 'dout3',
        'response': 'din3',
    },
}


class test_wrangler(object):
    """ Establish context for loading and resolving tests """

    def __init__(self, pins: Dict, dut: Dict, filepath: str):
        """ pins is a fully wrangled dictionary of all pins in the tester
            dut is the entry point to the comms to the DUT and other DUT info
        """
        self.pins = pins
        self.dut = dut
        self.function_map = {
            'digital_self_test': test_digital_to_digital,
        }
        self.test_plaintext = self._load_test_set(filepath)
        self.tests = self._resolve_test_set(self.test_plaintext)

    def _load_test_set(self, filepath: str) -> Dict:
        """ Load a set of tests from a test specification (source) 
            and return the plain-text tests as a dict with un-resolved functions
        """
        return test_spec

    def _resolve_test_set(self, plaintest: str) -> Dict:
        """ Resolve the functions in the incoming plain-text test document.
            Errors are fatal - as they are unresolvable and would invalidate the test.
        """
        resolvers = {
            'function': self._resolve_function,
        }

        test_set = plaintest
        for test_name, test_elem in test_set.items():
            for key, raw_value in test_elem.items():
                try:
                    resolved_value = resolvers[key](raw_value)
                    test_set[test_name][key] = resolved_value
                except KeyError:  # this is OK and expected
                    continue
        return test_set

    def _resolve_function(self, value: str) -> Callable:
        try:
            return self.function_map[value]
        except KeyError:  # this ins NOT OK and is not expected
            fatal("unknown function: {:}".format(value))


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute test_wrangler.py - EXITING")

'''
    'testM': {
        'display': "Test pin 3",
        'func': funcs.test_digital_to_digital,
        'set': self.pin.dout3.set,
        'read': self.pin.din3.read,
    },

    'testN': {
        'before': {},
        'stimulus': {
            'func': self.pin.dout3.set,
            'args': 1
        },
        'response': {
            'func': self.pin.din3.read,
            'args': None
        },
        'result': {},
        'after': {},
    }
'''