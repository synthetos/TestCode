""" pin.py

    Instantiate and operate a generic pin object

    Config look like:

    CONFIG_PIN = {
        "name": 'name',     # str:      name of pin - used for binding
        "type": 'IO',       # str:      one of: 'IO', 'ADC', 'DAC'
        "port": 0,          # int:      port or channel - if multi-port device
        "bit": 0,           # int:      bit position in port, 0-7
        "direction": 0,     # int:      0 = output, 1 = input
        "polarity": 0,      # int:      0 = non-inverted, 1=inverted
        "initial_value": 0, # int:      initial value (outputs only)
    }

"""
from typing import Dict, Callable

from util import fatal

VALID_PIN_TYPES = ['IO', 'ADC', 'DAC']

class pin(object):
    """ Configure and operate pin """

    def __init__(self, device: Callable, properties: Dict):
        """ Instantiate and initialize a pin object

            args:
                device - an instantiated device object to map the pin onto

                properties = {          # defines pin properties
                    'name': <str>       # pin must have a unique pin name
                    'type': <str>       # pin must be a VALID_PIN_TYPE
                    'port': <int>       # port on device (optional by device)
                    'bit': <int>        # bit position in port (optional by device)
                    'direction': <int>  # 0 = output, 1 = input (optional by device)
                    'polarity': <int>   # 0 = non-inverted, 1=inverted (opt by device)
                    'init': <int>       # initial value - for outputs only
                    'retry': <str>      # optional
                }
        """

        # defaults and sanity checks
        if 'name' not in properties:
            fatal("Pin has no name")  # alt: 'raise RuntimeError' - but it's fatal
        if 'type' not in properties or properties['type'] not in VALID_PIN_TYPES:
            fatal("Pin type error on {:}".format(properties['name']))
        properties['port'] = properties.setdefault('port', 0)
        properties['bit'] = properties.setdefault('bit', 0)
        properties['direction'] = properties.setdefault('direction', 0)
        properties['polarity'] = properties.setdefault('polarity', 0)
        properties['init'] = properties.setdefault('init', 0)
        properties['retry'] = properties.setdefault('retry', 0)

        self.device = device
        # self.properties = properties
        # self.name = properties['name']
        # self.type = properties['type']
        self.port = properties['port']
        self.bit = properties['bit']
        # self.direction = properties['direction']
        # self.polarity = properties['polarity']
        # self.init = properties['init']

        try:
            if device.type != properties['type']:  # cross check pin type and device type
                fatal("Pin type mismatch: device: {:}, pin: {:}".format(device.type, properties['type']))
        except ValueError:  # +++ insert proper exception once known
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
