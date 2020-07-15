""" device_dac5574.py

    DAC5574 Four channel Digital to Analog converter class

"""
from typing import Dict, Callable

from util import fatal


# Control byte: upper and lower nybles of control byte
#   these are combined and treated as if it were a device register address
CONTROL_MODE = 0x10  # Mode 01 - update addressed channel immediately
CONTROL_SELECT = [0x00, 0x02, 0x04, 0x06]  # Channels A, B, C, D


class dac5574(object):
    """
        These DAC I2C registers are a little wierd - using a "control byte" instead of
        independent registers. For simplicity we just consider the control byte to be
        a register address and treat it as such during I2C reads and writes
    """
    def __init__(self, bus: Callable, properties: Dict):

        self.bus = bus
        self.type = 'DAC'
        self.partno = 'dac5574'
        self.addr = properties['addr']
        self.shadow = [-2, -2, -2, -2]  # shadow DAC values: -2 means initialized but no pin
        self.reset()

    def reset(self):
        return

    # Native byte and bit manipulation for device registers
    #    Nothing here - see tca9539 if needed

    # Support for pin functions
    def init_pin(self, pin: Dict):
        """ Configure and initialize a DAC IO pin.
            There's nothing to configure at the pin level - so just cross-check
        """
        bit = pin['bit']
        if pin['type'] != 'DAC' or bit not in list(range(0, 4)):
            fatal("Pin misconfigation: {:}".format(pin['name']))
        self.shadow[bit] = -1  # -1 means pin iti but no value written yet

    def read_pin(self, port: int, bit: int, args={}):
        """ Return previously written value (shadow) or -1 if unwritten """
        return self.shadow[bit]

    def write_pin(self, port: int, bit: int, pin_value: int, args={}):
        """ Write analog value to mapped pin

            pin_value is provided as a scaled number relative to 'scale'.
            E.g. if scale == 3.3, then 1.65 will output 50% of DAC range
            (which happens to be 1.65 volts).
            Scale default is 3.3
        """
        scale = args.setdefault('scale', 3.3)
        value = int((pin_value / scale) * 255)
        control = CONTROL_MODE + CONTROL_SELECT[bit]
        self.bus.write_i2c_block_data(self.addr, control, [value, 0])
        self.shadow[bit] = pin_value

    def toggle_pin(self, port: int, bit: int, args={}):
        print("Attempt to toggle DAC pin")
        return None

    # Display functions (nothing to see here, move along)
    def show_ports(self):
        return

    def show_config(self):
        return


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute device_dac5574 class definition - EXITING")
