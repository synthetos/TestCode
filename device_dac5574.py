""" device_dac5574.py

    DAC5574 Four channel Digital to Analog converter class

"""
from typing import Dict, Callable
from smbus2 import SMBus, i2c_msg

from util import fatal

'''
CONFIG_DAC_1 = {
    'addr': 0x4D,               # FYI: 77 decimal
}
'''

# upper and lower nybles of control byte
CONTROL_MODE = 0x10
CONTROL_SELECT = [0x00, 0x02, 0x04, 0x06]

class dac5574(object):
    """
        These DAC I2C registers are a little wierd - using a "control byte" instead of
        independent registers. For simplicity we just consider the control byte to be
        a register address and treat it as such during I2C reads and writes
    """
    def __init__(self, bus: Callable, properties: Dict):

        self.partno = 'dac5574'
        self.type = 'DAC'
        self.bus = bus
        self.addr = properties['addr']
        self.reset()
        return

    def reset(self):
        return

    # ################################################
    # ### Native byte and bit manipulation for device
    # ################################################
    # Nothing here

    # ####################################
    # ### Support for pin class functions
    # ####################################
    def init_pin(self, pin: Dict):
        """ Configure and initialize a DAC IO pin.
            There's nothing to configure at the pin level - so just cross-check
        """
        bit = pin['bit']
        if pin['type'] != 'DAC' or bit not in list(range(0, 4)):
            fatal("Pin misconfigation: {:}".format(pin['name']))

    def read_pin(self, port: int, bit: int, args={}):
        print("Attempt to read DAC pin")
        return

    def write_pin(self, port: int, bit: int, pin_value: int, args={}):
        """ Write analog value to mapped pin 
        
            pin_value provided as 0.0 - 1.0
        """
        control = CONTROL_MODE + CONTROL_SELECT[bit]
        value = int(pin_value * 255)
        self.bus.write_i2c_block_data(self.addr, control, [value, 0])

    def toggle_pin(self, port: int, bit: int, args={}):
        print("Attempt to toggle DAC pin")
        return

    # ######################
    # ### display functions
    # ######################
    def show_ports(self):
        return

    def show_config(self):
        return


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute device_dac5574 class definition - EXITING")
