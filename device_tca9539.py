""" device_tca9539.py

    TCA9539 Sixteen bit IO Expander class

"""
from typing import Dict, Callable
from smbus2 import SMBus, i2c_msg

from util import fatal


CONFIG_DIN_0 = {
    "addr": 0x74,                   # 116 decimal
    "invert_0": 0b00000000,         # 0 is non-inverted, 1 is inverted
    "invert_1": 0b00000000,
    "config_0": 0b11111111,         # 0 is output pin, 1 is input pin
    "config_1": 0b11111111,
    "output_0": 0b00000000,         # initialization/reset value - 0 is LO
    "output_1": 0b00000000,
}

CONFIG_DIN_1 = {
    "addr": 0x75,                   # 117 decimal
    "invert_0": 0b00000000,         # 0 is non-inverted, 1 is inverted
    "invert_1": 0b00000000,
    "config_0": 0b11111111,         # 0 is output pin, 1 is input pin
    "config_1": 0b11111111,
    "output_0": 0b00000000,         # initialization/reset value - 0 is LO
    "output_1": 0b00000000,
}

CONFIG_DOUT = {
    "addr": 0x76,                   # 118 decimal
    "invert_0": 0b00000000,         # 0 is non-inverted, 1 is inverted
    "invert_1": 0b00000000,
    "config_0": 0b00000000,         # 0 is output pin, 1 is input pin
    "config_1": 0b00000000,
    "output_0": 0b00000000,         # initialization/reset value - 0 is LO
    "output_1": 0b00000000,
}

CONFIG_SPECIALS = {
    "addr": 0x77,                   # 119 decimal
    "invert_0": 0b00000000,         # 0 is non-inverted, 1 is inverted
    "invert_1": 0b00000000,
    "config_0": 0b00000000,         # 0 is output pin, 1 is input pin
    "config_1": 0b00000000,
    "output_0": 0b00000000,         # initialization/reset value - 0 is LO
    "output_1": 0b00000000,
}

REG_INPUT_0 = 0
REG_INPUT_1 = 1
REG_OUTPUT_0 = 2
REG_OUTPUT_1 = 3
REG_INVERT_0 = 4
REG_INVERT_1 = 5
REG_CONFIG_0 = 6
REG_CONFIG_1 = 7

class tca9539(object):

    def __init__(self, bus: Callable, properties: Dict):

        self.partno = 'tca9539'
        self.type = 'IO'
        self.bus = bus
        self.addr = properties['addr']
        self.init_output_0 = properties['output_0']  # init / reset values
        self.init_output_1 = properties['output_1']
        self.init_invert_0 = properties['invert_0']
        self.init_invert_1 = properties['invert_1']
        self.init_config_0 = properties['config_0']
        self.init_config_1 = properties['config_1']
        self.reset()
        return

    def reset(self):
        try:
            self.bus.write_byte_data(self.addr, REG_INVERT_0, self.init_invert_0)
            self.bus.write_byte_data(self.addr, REG_INVERT_1, self.init_invert_1)
            self.bus.write_byte_data(self.addr, REG_CONFIG_0, self.init_config_0)
            self.bus.write_byte_data(self.addr, REG_CONFIG_1, self.init_config_1)
            self.bus.write_byte_data(self.addr, REG_OUTPUT_0, self.init_output_0)
            self.bus.write_byte_data(self.addr, REG_OUTPUT_1, self.init_output_1)
            # data = [
            #     self.init_output_0, self.init_output_1,
            #     self.init_invert_0, self.init_invert_1,
            #     self.init_config_0, self.init_config_1,
            # ]
            # self.bus.write_byte_data(self.addr, REG_OUTPUT_0, data)

        except IOError as err:
            fatal("Failed to reset {:} err {:}".format(self.addr, err))

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

    # ################################
    # support for pin class functions
    #
    def init_pin(self, pin: Dict):
        """ Configure and initialize a digital IO pin.
            See pin object for 'pin' dictionary structure 
        """
        port = pin['port']
        bit = pin['bit']
        if pin['type'] != 'IO' or port not in [0, 1] or bit not in list(range(0, 8)):
            fatal("Pin misconfigation: {:}".format(pin['name']))

        # update the device registers and shadow init values
        self.write_bit((REG_CONFIG_0 + port), bit, pin['direction'])
        self.write_attr_bit((REG_CONFIG_0 + port), bit, pin['direction'])

        self.write_bit((REG_INVERT_0 + port), bit, pin['polarity'])
        self.write_attr_bit((REG_INVERT_0 + port), bit, pin['polarity'])

        # set initial output state if output bit 
        if pin['direction'] == 0:
            self.write_bit((REG_OUTPUT_0 + port), bit, pin['init'])
            self.write_attr_bit((REG_OUTPUT_0 + port), bit, pin['init'])

    def read_pin(self, port: int, bit: int, args={}) -> int:
        """ read a pin (bit) in an input register: return 0 or 1 """
        byte = self.bus.read_byte_data(self.addr, (REG_INPUT_0 + port))
        return int(byte & (1 << bit) > 0)

    def write_pin(self, port: int, bit: int, bit_value: int, args={}):
        """ Set/clear a bit in an output register """
        self.write_bit((REG_OUTPUT_0 + port), bit, bit_value, args)

    def toggle_pin(self, port: int, bit: int, args={}):
        """ Toggle a bit in an output register """
        byte = self.bus.read_byte_data(self.addr, (REG_OUTPUT_0 + port))
        byte = byte ^ (1 << bit)
        self.bus.write_byte_data(self.addr, (REG_OUTPUT_0 + port), byte)

    # ###################
    # display functions
    #
    def show_ports(self):
        try:
            # p0 = self.bus.read_byte_data(self.addr, REG_INPUT_0)
            # p1 = self.bus.read_byte_data(self.addr, REG_INPUT_1)
            p0, p1 = self.bus.read_i2c_block_data(self.addr, REG_INPUT_0, 2)
        except IOError as err:
            print("Failed to read port {:} err {:}".format(self.addr, err))
            return False

        print("Device: {:}, Addr: Ox{:02X}, Ports Ox{:02X}{:02X}".format(self.partno, self.addr, p1, p0))

    def show_config(self):
        try:
            print("Device: {:}, Addr: 0x{:02X}, Config 0x{:02X}{:02X}, Invert 0x{:02X}{:02X}".format(
                self.partno, self.addr,
                self.bus.read_byte_data(self.addr, REG_CONFIG_1),
                self.bus.read_byte_data(self.addr, REG_CONFIG_0),
                self.bus.read_byte_data(self.addr, REG_INVERT_1),
                self.bus.read_byte_data(self.addr, REG_INVERT_0)))
            return True
        except IOError as err:
            print("Failed to read configs {:} err {:}".format(self.addr, err))
            return False

# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute device_tca9539 class definition - EXITING")
