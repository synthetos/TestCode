""" main.py - entry point for tester


"""
from typing import Dict

import qwiic_i2c
from smbus2 import SMBus, i2c_msg


""" 1=input, 0=output"""
config_0 = 0b00010000
config_1 = 0b01010101

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