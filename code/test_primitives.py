""" test_primitives.py

    Low level functions useful for creating tests
"""
from typing import Dict  # Callable


def test_digital_to_digital(self, args: Dict) -> str:
    """ Test a digital outout connected to a digital input line.
        This is a specialized test that's only meaningdful to self-r=test the baseboared

        args = {
            'set': Callable,    # output pin.set() function
            'read': Callable,   # input pin.read() function
        }
        returns: 'pass', 'fail', 'error'
    """
    try:
        args['set'](1)
        one = args['read']()
        args['set'](0)
        zero = args['read']()
        if one == 1 and zero == 0:
            return 'pass'
        else:
            return 'fail'
    except IndexError:
        return 'error'


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute util.py - EXITING")
