""" pin.py

    Instantiate and operate a generic pin object
    See pin_assignments.py for the structure of configuration dictionaries
"""

from typing import Dict, Callable
from util import fatal
from logger import get_logger

log = get_logger()

VALID_PIN_TYPES = ['IO', 'ADC', 'DAC']


class pin(object):
    """ Configure and operate pin """

    def __init__(self, device: Callable, properties: Dict):
        """ Instantiate and initialize a pin object """

        if 'type' not in properties or properties['type'] not in VALID_PIN_TYPES:
            fatal("Pin type error on {:}".format(properties['name']))
        try:
            if device.type != properties['type']:  # cross check pin type and device type
                fatal("Pin type mismatch: device: {:}, pin: {:}".format(device.type, properties['type']))
        except ValueError:  # +++ device class does not exist: insert proper exception once known
            fatal("Device not found for pin: {:}".format(properties['name']))

        self.device = device
        self.port = properties.setdefault('port', 0)
        self.bit = properties.setdefault('bit', 0)
        # self.direction = properties.setdefault('direction', 0)
        # self.polarity = properties.setdefault('polarity', 0)
        # self.init = properties.setdefault('init', 0)
        # self.retry = properties.setdefault('retry', 0)
        self.comment = properties.setdefault('comment', '')
        self.args = properties  # preserve the properties dictionary as function args

        # initialize pin using code in the underlying device
        device.init_pin(properties)  # errors are fatal and handled by device

    def read(self, pin_value=None):
        return self.device.read_pin(self.port, self.bit, self.args)

    def write(self, pin_value: int):
        self.device.write_pin(self.port, self.bit, pin_value, self.args)

    def set(self, pin_value=1):  # polymorphic for digital and analog set
        self.device.write_pin(self.port, self.bit, pin_value, self.args)

    def clear(self, pin_value=0):
        self.device.write_pin(self.port, self.bit, 0, self.args)

    def toggle(self, pin_value=None):
        self.device.toggle_pin(self.port, self.bit, self.args)


# ############################
# ### Pin lookup functions ###
# ############################

def pinf(pins: Dict, name: str) -> Callable:
    """ Return pin onject by name """
    try:
        return pins['name']
    except IndexError:
        log.warning("unknown pin name")
        return None

'''
def pin_func(pins: Dict, name: str, func: str, value=None) -> Callable:
    """ Execute the pin function without haveing the pin object itself. """
    funcs = {
        'read': pin.read(),
        'write': pin.write(value),
        'set': pin.write(value),
        'clear': pin.write(),
        'toggle': pin.write()
    }
    try:
        pin = pins['name']
    except IndexError:
        log.warning("unknown pin name")

    return 
'''

# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute pin class definition - EXITING")
