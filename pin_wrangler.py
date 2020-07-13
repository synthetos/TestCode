""" pin_wrangler.py

    Instantiate pins from pin_assignments
    Requires device objects be created first (run device_wrangler)

"""

from pin_assignments import PIN_ASSIGNMENTS
from pin import pin


class pins(object):

    def __init__(self, devices):

        self.pins = {}
        # self.device = devices  # leave this here for now

        print('Initializing Pins')
        for name, properties in PIN_ASSIGNMENTS.items():
            device = devices.devices[properties['device']]
            self.pins[name] = pin(device, properties)        # add to dict of all pins
            object.__setattr__(self, name, self.pins[name])  # make pin accessible by p.<name>
            print("  Initialized pin {:8}  {:}".format(name, properties['comment']))

# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute pin_wrangler class definition - EXITING")
