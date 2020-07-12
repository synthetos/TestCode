""" device_dac5574.py

    DAC5574 Four channel Digital to Analog converter class

"""
from typing import Dict, Callable
from smbus2 import SMBus, i2c_msg

from util import fatal

# upper and lower nybles of control byte
CHANNEL_LOAD = 0x10
CHANNEL_SELECT = [0x00, 0x02, 0x04, 0x06]


CONFIG_DAC_1 = {
    'addr': 0x4D,               # FYI: 77 decimal
}

class dac5574(object):

    def __init__(self, bus: Callable, properties: Dict):

        self.partno = 'dac5574'
        self.type = 'DAC'
        self.bus = bus
        self.addr = properties['addr']
        self.reset()
        return

    def reset(self):
        return

    ''' Unused
    def write_attr_bit(self, byte: int, bit: int, bit_value: int):
        """ Set or clear a bit in a byte variable to bit_value """
        if bit_value == 1:
            byte |= (1 << bit)
        else:
            byte &= ~(0 << bit)

    def write_byte(self, register: int, byte: int):
        """ Write an byte value to a device register """
        try:
            self.bus.write_byte_data(self.addr, register, byte)
        except IOError as err:
            fatal("Failed write_bit addr:{:02X} err {:}".format(self.addr, err))

    def set_bit(self, register: int, bit: int, args={}):
        """ Set bit 0-7 in device register (e.g. port) """
        mask = 1 << bit
        byte = self.bus.read_byte_data(self.addr, register)
        self.bus.write_byte_data(self.addr, register, byte | mask)

    def clear_bit(self, register: int, bit: int, args={}):
        """ Clear bit 0-7 in device register (e.g. port) """
        mask = 1 << bit
        byte = self.bus.read_byte_data(self.addr, register)
        self.bus.write_byte_data(self.addr, register, byte & ~mask)

    def write_bit(self, register: int, bit: int, bit_value: int, args={}):
        """ Set or clear a bit in device register to bit_value """
        mask = 1 << bit
        byte = self.bus.read_byte_data(self.addr, register)
        if bit_value == 1:
            self.bus.write_byte_data(self.addr, register, byte | mask)
        else:
            self.bus.write_byte_data(self.addr, register, byte & ~mask)
    '''

    # ################################
    # support for pin class functions
    #
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
        control = CHANNEL_LOAD + CHANNEL_SELECT[bit]
        value = int(pin_value * 255)
        self.bus.write_i2c_block_data(self.addr, control, [value, 0])

    def toggle_pin(self, port: int, bit: int, args={}):
        print("Attempt to toggle DAC pin")
        return

    # ###################
    # display functions
    #
    def show_ports(self):
        return

    def show_config(self):
        return

# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute device_dac5574 class definition - EXITING")
