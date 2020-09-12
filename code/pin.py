""" pin.py

    Instantiate and operate a generic pin object
    See pin_assignments.py for the structure of configuration dictionaries

"""
from typing import Dict, Callable

from util import fatal

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

    def read(self):
        return self.device.read_pin(self.port, self.bit, self.args)

    def write(self, pin_value: int):
        self.device.write_pin(self.port, self.bit, pin_value, self.args)

    def set(self, pin_value=1):  # polymorphic for digital and analog set
        self.device.write_pin(self.port, self.bit, pin_value, self.args)

    def clear(self):
        self.device.write_pin(self.port, self.bit, 0, self.args)

    def toggle(self):
        self.device.toggle_pin(self.port, self.bit, self.args)


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute pin class definition - EXITING")
