""" main.py - entry point for tester


"""
from typing import Dict

import qwiic_i2c
from smbus2 import SMBus, i2c_msg

from device_tca9539 import tca9539
from device_tca9539 import CONFIG_DIN_0, CONFIG_DIN_1, CONFIG_DOUT, CONFIG_SPECIALS


""" 1=input, 0=output"""
config_0 = 0b00010000
config_1 = 0b01010101

def main():
    """ Entry point for tester """

    bus = SMBus(1)
    din0 = tca9539(bus, CONFIG_DIN_0)
    din1 = tca9539(bus, CONFIG_DIN_1)
    dout = tca9539(bus, CONFIG_DOUT)
    specials = tca9539(bus, CONFIG_SPECIALS)

    # Open i2c bus 1 and read one byte from address 0x77, offset 0
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