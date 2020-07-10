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
        """ Instantiate and initialize a pin object according to:

            device - must be an instantiated device object underlying the pin

            config = {              # defines pin properties
                'name': <str>       # must have a unique pin name
                'type': <str>       # must be a VALID_PIN_TYPE
                'port': <int>       # optional depending on device
                'bit': <int>        # optional depending on device
                'direction': <int>  # optional: 0 = output, 1 = input
                'polarity': <int>   # optional: 0 = non-inverted, 1=inverted
                'init': <int>       # optional: initial value for outputs only
                'retry': <str>      # optional depending on device
            }
        """

        # defaults and sanity checks
        if 'name' not in properties:
            fatal("Pin config has no name - EXITING")  # alt: 'raise RuntimeError' - but it's fatal
        if 'type' not in properties or properties['type'] not in VALID_PIN_TYPES:
            fatal("Pin type error for {:}".format(properties['name']))
        properties['port'] = properties.setdefault('port', 0)
        properties['bit'] = properties.setdefault('port', 0)
        properties['direction'] = properties.setdefault('direction', 0)
        properties['polarity'] = properties.setdefault('polarity', 0)
        properties['init'] = properties.setdefault('init', 0)
        properties['retry'] = properties.setdefault('retry', 0)

        self.device = device
        self.properties = properties

        try:
            if device.type != properties['type']:  # cross check pin type and device type
                fatal("Pin type mismatch: device: {:}, pin: {:}".format(device.type, properties['type']))
        except ValueError:  # +++ insert proper exception once known
            fatal("Device not found for pin: {:}".format(properties['name']))

        # initialize pin using code in the underlying device
        try:
            device.init_pin(properties)
        except RuntimeError:
            print("Unable to configure pin {:} on device {:}".format(
                properties['name'], self.device.partno))
            raise RuntimeError

# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute pin class definition - EXITING")
