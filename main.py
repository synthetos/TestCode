""" main.py - entry point for tester


"""
import qwiic_i2c
from smbus2 import SMBus, i2c_msg


""" 1=input, 0=output"""
config_0 = 0b00010000
config_1 = 0b01010101


class tca9539(object):

    INPUT_0 = 0
    INPUT_1 = 1
    OUTPUT_0 = 2
    OUTPUT_1 = 3
    INVERT_0 = 4
    INVERT_1 = 5
    CONFIG_0 = 6
    CONFIG_1 = 7

    def __init__(self, bus, addr, invert_0, invert_1, config_0, config_1):

        self.bus = bus
        self.addr = addr
        self.input_0 = 0    # 0 is low
        self.input_1 = 0
        self.output_0 = 0   # 0 is low
        self.output_1 = 0
        self.invert_0 = invert_0   # 0 is non-inverted, 1 is inverted
        self.invert_1 = invert_1
        self.config_0 = config_0   # 0 is output pin, 1 is input pin
        self.config_1 = config_1

    def reset(self):
        try:
            bus.write_byte_data(self.addr, )


    def show_tca9539(addr: int):
        b = bus.read_byte_data(addr, i)
        print("Read back {:}".format(b))



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