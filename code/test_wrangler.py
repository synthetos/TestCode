""" test_wrangler.py

    This module collects tests and returns a test_set dictionary.

    The wrangler's job is to load abstract definitions for the tests
    and resolve them into executable functions that the sequencer / runner
    can execute directly.

    As such - it needs to know the functions for all these tests,
    so as test types are added they need to be added to the loader.

    To add a new test type include and document it in the loader
    and add it to the function_map in the __init__

    Test document structure:

    test_set: {             # name of whole test set (string)
        test_name_1: {},    # name of first test (string)
        test_name_2: {},
        ...
        test_name_N: {}     # name of Nth test (string)
    }

    Test structure:
        The [R] means this is a required field for all tests.
        Requirements for all other fields are set by the selected function.
        The 'test' dict will be passed to the test function for interpretation.
        Most of the elements in the test dict are by convention. See Attribute Conventions

    test_name: {                # name of test (string, req)
        'test': { [R]           # dictionary specifying the test
            'display': str [R]  # string to display when running test
            'comment': str      # additional comment (in JSON) - will not be displayed
            'function': str [R] # name of test function to run (i.e. not the function ppinter)
            'stimulus': str     # pin or action to initiate test (see conventions)
            'response': str     # pin or channel to receive response (see conventions)
            'pattern': str      # pattern to match to determine result
            'control': str      # supports skip, end and other controls
            ...other: Any       # other args may be used by specific test functions
        }
        'results': {
            'passfail': ""      # function returns 'pass' or 'fail' (null string on entry)
            'message': ""       # additional message returned by function
            ...other: Any       # other data may be returned by specific test functions
        }
        # optional - not implemented
        'before': {             # function and args to run before test (optional)
            'function': str
            '_args_': str
        }
        'post_pass': {          # function and args to run after passed test (optional)
            'function': str
            '_args_': str
        }
        'post_fail': {          # fucntion and args to run after failed test (optional)
            'function': str
            'args': {}
        }
    }

    Attribute Conventions:
    - function: see test_functions for complete set of supported test functions

    - stimulus: the valid form depends on the function. Conventions are:
        ">{JSON} or Gcode or whatever"
                    Any string prefixed by '>' is interpreted as a string that can be sent to the DUT.
                    Spaces trailing the '>' are removed.

        "dout2"     Output pin
                    Any non-prefixed string is interpreted as an output pin,
                    and is validated against pins dictionary for existence & direction.
                    If a value is required (e.g. for a DAC) it must be passed
                    in the function args as 'value': float | int | a list of same

    - response: the valid form depends on the function. Conventions are:
        "<{JSON} or Gcode or whatever"
                    Any string prefixed by '<' is interpreted as a string that can be received from the DUT.
                    Spaces trailing the '<' are removed.

        "din2"      Input pin
                    Any non-prefixed string is interpreted as an input pin,
                    and is validated against pins dictionary for existence & direction.

"""
from typing import Dict, Callable

from util import fatal
from logger import get_logger

# Test Functions
# These functions are not actually called - they are used to validate tests
from test_functions import test_digital_to_digital     # self-test of the tester board itself


log = get_logger()


# Temporary definition for a test before I get the JSON load functions going
test_set = {
    'test_pin3': {
        'test': {
            'display': "Test pin 3",
            'function': 'test_digital_to_digital',
            'stimulus': 'dout3',
            'response': 'din3',
        }
    }
}


class test_wrangler(object):
    """ Establish context for loading and resolving tests """

    def __init__(self, pins: Dict, dut: Dict, filepath: str):
        """ pins is a fully wrangled dictionary of all pins in the tester
            dut is the entry point to the comms to the DUT and other DUT info
        """
        self.pins = pins
        self.dut = dut
        self.tests = self._load_tests(filepath)
        self.tests = self._validate_tests(self.tests)

    def _load_tests(self, filepath: str) -> Dict:
        """ Load a set of tests from a test specification (source) 
            and return the plain-text tests as a dict with un-resolved functions
        """
        return test_set

    def _validate_tests(self, tests: str):
        """ Perform basic validation on the loaded test set.
            Verify that function exists, 
            and that stimulus and response exist and follow conventions.
            Errors are fatal - as they are unresolvable and would invalidate the test.
        """
        validators = {
            'function': self._validate_function,
            'stimulus': self._validate_stimulus,
            'response': self._validate_response,
        }

        for test_name, test_structs in tests.items():
            test = test_structs['test']
            for key, value in test.items():
                try:
                    validators[key](value)
                except KeyError:  # this is OK and expected
                    continue

        return test_set

    def _validate_function(self, function_name: str):
        """ eval() converts the name of the function into a function object
            Fail validation if the function is not found
        """
        try:
            eval(function_name)
        except NameError:
            fatal("Test function not found: {:}".format(function_name))

    def _validate_stimulus(self, stimulus_name: str):
        if stimulus_name[0] == '>':
            return
        try:
            getattr(self.pins, stimulus_name)
        except AttributeError:
            fatal("Stimulus pin not found: {:}".format(stimulus_name))

    def _validate_response(self, response_name: str):
        if response_name[0] == '<':
            return
        try:
            getattr(self.pins, response_name)
        except AttributeError:
            fatal("Response pin not found: {:}".format(response_name))


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