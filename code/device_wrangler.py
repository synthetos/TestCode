""" device_wrangler.py

    Instantiate devices and perform inital configuration

"""

# from typing import Dict
from smbus2 import SMBus, i2c_msg


class device_wrangler(object):

    def __init__(self, device_assignments):

        self.bus = SMBus(1)
        self.devices = {}

        print('Initializing Devices')
        for name, properties in device_assignments.items():
            self.devices[name] = properties['device'](self.bus, properties)
            print("  Initialized {:12}  {:}".format(name, properties['comment']))


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute device_wrangler class definition - EXITING")

