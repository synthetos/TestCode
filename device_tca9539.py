""" device_tca9539.py

    Classes for IO Expander TCA9539

"""
from typing import Dict, Callable
# import qwiic_i2c
from smbus2 import SMBus, i2c_msg


REG_INPUT_0 = 0
REG_INPUT_1 = 1
REG_OUTPUT_0 = 2
REG_OUTPUT_1 = 3
REG_INVERT_0 = 4
REG_INVERT_1 = 5
REG_CONFIG_0 = 6
REG_CONFIG_1 = 7

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
    "config_0": 0b00010000,         # 0 is output pin, 1 is input pin
    "config_1": 0b01010101,
    "output_0": 0b00000000,         # initialization/reset value - 0 is LO
    "output_1": 0b00000000,
}


class tca9539(object):

    def __init__(self, bus: Callable, config: Dict):

        self.partno = 'tca9539'
        self.type = 'IO'
        self.bus = bus
        self.addr = config['addr']
        self.output_0 = config['output_0']  # initlaization / reset value
        self.output_1 = config['output_1']
        self.invert_0 = config['invert_0']
        self.invert_1 = config['invert_1']
        self.config_0 = config['config_0']
        self.config_1 = config['config_1']
        self.reset()
        return

    def reset(self) -> bool:
        try:
            self.bus.write_byte_data(self.addr, REG_INVERT_0, self.invert_0)
            self.bus.write_byte_data(self.addr, REG_INVERT_1, self.invert_1)
            self.bus.write_byte_data(self.addr, REG_CONFIG_0, self.config_0)
            self.bus.write_byte_data(self.addr, REG_CONFIG_1, self.config_1)
            self.bus.write_byte_data(self.addr, REG_OUTPUT_0, self.output_0)
            self.bus.write_byte_data(self.addr, REG_OUTPUT_1, self.output_1)
            # data = [
            #     self.output_0, self.output_1,
            #     self.invert_0, self.invert_1,
            #     self.config_0, self.config_1,
            # ]
            # self.bus.write_byte_data(self.addr, REG_OUTPUT_0, data)

        except IOError as err:
            print("Failed to reset {:} err {:}".format(self.addr, err))
            return False
        return True

    def init_pin(self, properties: Dict):
        """ Configure and initialize a digital IO pin. 
            See pin object for config dictionary structure 
        """
        if properties['type'] != 'IO' or \
           properties['port'] not in [0, 1] or \
           properties['bit'] not in range(0, 7):
            raise RuntimeError

        

    def show_config(self):
        try:
            print("Addr: 0x{:02X} Config 0x{:02X}{:02X}  Invert 0x{:02X}{:02X}".format(
                self.addr,
                self.bus.read_byte_data(self.addr, REG_CONFIG_1),
                self.bus.read_byte_data(self.addr, REG_CONFIG_0),
                self.bus.read_byte_data(self.addr, REG_INVERT_1),
                self.bus.read_byte_data(self.addr, REG_INVERT_0)))
            return True
        except IOError as err:
            print("Failed to read configs {:} err {:}".format(self.addr, err))
            return False

    def write_byte(self, port: int, value: int):
        """ Write an output byte value to port 0 or 1 """
        register = REG_OUTPUT_0 + port
        try:
            self.bus.write_byte_data(self.addr, register, value)
        except IOError as err:
            print("Failed write_bit addr:{:02X} err {:}".format(self.addr, err))
            return False
        return True       

    def set_bit(self, port: int, position: int):
        """ Set output bit at port 0-1 / position 0-7 """
        register = REG_OUTPUT_0 + port
        try:
            self.bus.write_byte_data(self.addr, register, value)
        except IOError as err:
            print("Failed write_bit addr:{:02X} err {:}".format(self.addr, err))
            return False
        return True       

    def write_bit(self, position: int, value: bool):
        """ Set or clear a bit at position 0-15 """
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
            print("Failed write_bit addr:{:02X} err {:}".format(self.addr, err))
            return False
        return True

    def show_ports(self):
        try:
            # p0 = self.bus.read_byte_data(self.addr, REG_INPUT_0)
            # p1 = self.bus.read_byte_data(self.addr, REG_INPUT_1)
            p0, p1 = self.bus.read_i2c_block_data(self.addr, REG_INPUT_0, 2)
        except IOError as err:
            print("Failed to read port {:} err {:}".format(self.addr, err))
            return False

        print("Addr: Ox{:02X} Ports Ox{:02X}{:02X}".format(self.addr, p1, p0))


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute device_tca9539 class definition - EXITING")
