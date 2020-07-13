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
        properties['port'] = properties.setdefault('port', 0)
        properties['bit'] = properties.setdefault('bit', 0)
        properties['direction'] = properties.setdefault('direction', 0)
        properties['polarity'] = properties.setdefault('polarity', 0)
        properties['init'] = properties.setdefault('init', 0)
        properties['retry'] = properties.setdefault('retry', 0)
        properties['comment'] = properties.setdefault('comment', '')

        self.device = device
        self.port = properties['port']
        self.bit = properties['bit']
        # self.direction = properties['direction']  # in case this becomes useful at some point
        # self.polarity = properties['polarity']
        # self.init = properties['init']
        self.comment = properties['comment']

        try:
            if device.type != properties['type']:  # cross check pin type and device type
                fatal("Pin type mismatch: device: {:}, pin: {:}".format(device.type, properties['type']))
        except ValueError:  # +++ device class does not exist: insert proper exception once known
            fatal("Device not found for pin: {:}".format(properties['name']))

        # initialize pin using code in the underlying device
        device.init_pin(properties)  # errors are fatal and handled by device

    def read(self):
       return self.device.read_pin(self.port, self.bit)

    def write(self, pin_value: int):
       self.device.write_pin(self.port, self.bit, pin_value)

    def set(self):
        self.device.write_pin(self.port, self.bit, 1)

    def clear(self):
        self.device.write_pin(self.port, self.bit, 0)

    def toggle(self):
       self.device.toggle_pin(self.port, self.bit)


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute pin class definition - EXITING")
