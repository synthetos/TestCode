import qwiic_i2c
from smbus2 import SMBus, i2c_msg

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
