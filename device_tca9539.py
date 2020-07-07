""" device_tca9539.py - classes for IO Expander TCA9539

"""
from typing import Dict, Callable
import qwiic_i2c
from smbus2 import SMBus, i2c_msg


REG_INPUT_0 = 0
REG_INPUT_1 = 1
REG_OUTPUT_0 = 2
REG_OUTPUT_1 = 3
REG_INVERT_0 = 4
REG_INVERT_1 = 5
REG_CONFIG_0 = 6
REG_CONFIG_1 = 7

DIGITAL_IN_0_CONFIG = {
    "addr": 0x74,
    "invert_0": 0b00000000,         # 0 is non-inverted, 1 is inverted
    "invert_1": 0b00000000,
    "config_0": 0b11111111,         # 0 is output pin, 1 is input pin
    "config_1": 0b11111111,
    "output_0_init": 0b00000000,    # 0 is low
    "output_1_init": 0b00000000,
}

DIGITAL_IN_1_CONFIG = {
    "addr": 0x75,
    "invert_0": 0b00000000,         # 0 is non-inverted, 1 is inverted
    "invert_1": 0b00000000,
    "config_0": 0b11111111,         # 0 is output pin, 1 is input pin
    "config_1": 0b11111111,
    "output_0_init": 0b00000000,    # 0 is low
    "output_1_init": 0b00000000,
}

DIGITAL_OUT_CONFIG = {
    "addr": 0x76,
    "invert_0": 0b00000000,         # 0 is non-inverted, 1 is inverted
    "invert_1": 0b00000000,
    "config_0": 0b00000000,         # 0 is output pin, 1 is input pin
    "config_1": 0b00000000,
    "output_0_init": 0b00000000,    # 0 is low
    "output_1_init": 0b00000000,
}

SPECIALS_CONFIG = {
    "addr": 0x77,
    "invert_0": 0b00000000,         # 0 is non-inverted, 1 is inverted
    "invert_1": 0b00000000,
    "config_0": 0b00010000,         # 0 is output pin, 1 is input pin
    "config_1": 0b01010101,
    "output_0_init": 0b00000000,    # 0 is low
    "output_1_init": 0b00000000,
}


class tca9539(object):

    def __init__(self, bus: Callable, config: Dict):

        self.bus = bus
        self.addr = config['addr']
        self.input_0 = 0
        self.input_1 = 0
        self.output_0 = config['output_0_init']
        self.output_1 = config['output_1_init']
        self.invert_0 = config['invert_0']
        self.invert_1 = config['invert_1']
        self.config_0 = config['config_0']
        self.config_1 = config['config_1']

    def reset(self) -> bool:
        try:
            # self.bus.write_byte_data(self.addr, REG_INVERT_0, self.invert_0)
            # self.bus.write_byte_data(self.addr, REG_INVERT_1, self.invert_1)
            # self.bus.write_byte_data(self.addr, REG_CONFIG_0, self.config_0)
            # self.bus.write_byte_data(self.addr, REG_CONFIG_1, self.config_1)
            # self.bus.write_byte_data(self.addr, REG_OUTPUT_0, self.output_0_init)
            # self.bus.write_byte_data(self.addr, REG_OUTPUT_1, self.output_1_init)
            data = [
                self.output_0_init, self.output_1_init,
                self.invert_0, self.invert_1, self.config_0, self.config_1,
            ]
        except IOError as err:
            print("Failed to reset {:} err {:}".format(self.addr, err))
            return False
        return True

    def write_bit(self, position: int, value: bool):
        """ Perform a read-modify-write bit operation
            position is bit position 0-15
        """
        if position < 8:
            register = REG_OUTPUT_0
        else:
            register = REG_OUTPUT_1
            position -= 8
        mask = 1 << position
        try:
            byte = self.bus.read_byte_data(self.addr, register)
            if value == 1:
                new = byte | mask
                self.bus.write_byte_data(self.addr, register, new)
            else:
                new = byte & ~mask
                self.bus.write_byte_data(self.addr, register, new)
        except IOError as err:
            print("Failed write {:x}.{:} err {:}".format(self.addr, bit, err))
            return False


    def show_configs(self):
        try:
            # i0 = self.bus.read_byte_data(self.addr, REG_INVERT_0)
            # i1 = self.bus.read_byte_data(self.addr, REG_INVERT_1)
            # c0 = self.bus.read_byte_data(self.addr, REG_CONFIG_0)
            # c1 = self.bus.read_byte_data(self.addr, REG_CONFIG_1)
            i0, i1, c0, c1 = read_i2c_block_data(self.addr, REG_INVERT_0, 4)

        except IOError as err:
            print("Failed to read configs {:} err {:}".format(self.addr, err))
            return False
        print("Config {:x}: {:x}.{:x}  Invert {:x}.{:x}".format(self.addr, c0, c1, i0, i1))

    def show_ports(self):
        try:
            # p0 = self.bus.read_byte_data(self.addr, REG_INPUT_0)
            # p1 = self.bus.read_byte_data(self.addr, REG_INPUT_1)
            p0, p1 = read_i2c_block_data(self.addr, REG_INPUT_0, 2)
       except IOError as err:
            print("Failed to read port {:} err {:}".format(self.addr, err))
            return False
        print("Port {:x}: {:x}.{:x}".format(self.addr, port_0, port_1))


def main():
    # Open i2c bus 1 and read one byte from address 0x77, offset 0
    bus = SMBus(1)
    addrs = [0x74, 0x77]
    try:
        for addr in addrs:
            print("Addr: {:}".format(addr))
            for i in range(7):
                b = bus.read_byte_data(addr, i)
                print("Read back {:}".format(b))
    except IOError as err:
        print("Failed to connect to {:} err {:}".format(addr, err))

    bus.close()

# Do Not Delete
if __name__ == "__main__":
    main()