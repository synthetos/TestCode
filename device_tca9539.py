""" device_tca9539.py

    TCA9539 Sixteen bit IO Expander class

"""
from typing import Dict, Callable

from util import fatal


# register assignments
REG_INPUT_0 = 0x00
REG_INPUT_1 = 0x01
REG_OUTPUT_0 = 0x02
REG_OUTPUT_1 = 0x03
REG_INVERT_0 = 0x04
REG_INVERT_1 = 0x05
REG_CONFIG_0 = 0x06
REG_CONFIG_1 = 0x07


class tca9539(object):

    def __init__(self, bus: Callable, properties: Dict):

        self.bus = bus
        self.type = 'IO'
        self.partno = 'tca9539'
        self.addr = properties['addr']
        self.reset()
        return

    def reset(self):
        try:
            inits = [0, 0, 0, 0, 0, 0]  # initialize all registers but INPUT to 0
            self.bus.write_i2c_block_data(self.addr, REG_OUTPUT_0, inits)
        except IOError as err:
            fatal("Failed to reset {:} err {:}".format(self.addr, err))

    # Native byte and bit manipulation for device
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

    # Support for pin functions
    def init_pin(self, pin: Dict):
        """ Configure and initialize a digital IO pin.
            See pin object for 'pin' dictionary structure
        """
        port = pin['port']
        bit = pin['bit']
        if pin['type'] != 'IO' or port not in [0, 1] or bit not in list(range(0, 8)):
            fatal("Pin misconfigation: {:}".format(pin['name']))

        # update the device registers
        self.write_bit((REG_CONFIG_0 + port), bit, pin['direction'])
        self.write_bit((REG_INVERT_0 + port), bit, pin['polarity'])
        if pin['direction'] == 0:  # set initial output state if output bit
            self.write_bit((REG_OUTPUT_0 + port), bit, pin['init'])

    def read_pin(self, port: int, bit: int, args={}) -> int:
        """ read a input pin (bit) or return value of output pin """
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

    # Display functions
    def show_ports(self):
        try:
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
