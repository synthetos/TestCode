""" device_adc128d818.py

    ADC128D818 Eight channel Analog to Digital converter class

"""
from typing import Dict, Callable

from util import fatal


# register assignments
# Note: did not define manufacturer ID or revision ID registers
REG_CONFIGURATION = 0x00
REG_INTERRUPT_STATUS = 0x01
REG_INTERRUPT_MASK = 0x02
REG_CONVERSION_RATE = 0x07
REG_CHANNEL_DISABLE = 0x08
REG_ONE_SHOT = 0x09
REG_DEEP_SHUTDOWN = 0x0A
REG_ADVANCED_CONFIGURATION = 0x0B
REG_BUSY_STATUS = 0x0C
REG_READINGS_BASE = 0x20        # base register address for 8 channel readings registers
REG_LIMIT_BASE = 0x2A           # base register address for 8 channel limit registers


class adc128d818(object):

    def __init__(self, bus: Callable, properties: Dict):

        self.bus = bus
        self.type = 'ADC'
        self.partno = 'adc128d818'
        self.addr = properties['addr']
        self.configuration = properties['configuration']  # init / reset values shadow properties dict
        self.interrupt_mask = properties['interrupt_mask']
        self.conversion_rate = properties['conversion_rate']
        self.channel_disable = properties['channel_disable']
        self.deep_shutdown = properties['deep_shutdown']
        self.advanced_configuration = properties['advanced_configuration']

        if (self.advanced_configuration & 0x01) == 1:
            self.vref = 3.3     # if bit is set vref is used for ADC reference
        else:
            self.vref = 2.56    # if bit is not set internal 2.56v reference is used
        self.reset()
        return

    def reset(self):
        """ Reset device to initial conditions as per self.init... variables
            Start by writing 0x80 to CONFIGURATION, which initializes the device,
            then load the configurations, then set CONFIGURATION register to START value
        """
        try:
            self.bus.write_byte_data(self.addr, REG_CONFIGURATION, 0x80)  # initialize
            self.bus.write_byte_data(self.addr, REG_INTERRUPT_MASK, self.interrupt_mask)
            self.bus.write_byte_data(self.addr, REG_CONVERSION_RATE, self.conversion_rate)
            self.bus.write_byte_data(self.addr, REG_CHANNEL_DISABLE, self.channel_disable)
            self.bus.write_byte_data(self.addr, REG_DEEP_SHUTDOWN, self.deep_shutdown)
            self.bus.write_byte_data(self.addr, REG_ADVANCED_CONFIGURATION, self.advanced_configuration)
            self.bus.write_byte_data(self.addr, REG_CONFIGURATION, self.configuration)
        except IOError as err:
            fatal("Failed to reset {:} err {:}".format(self.addr, err))

    # Native byte and bit manipulation for device registers
    #    Nothing here - see tca9539 if needed

    # Support for pin functions
    def init_pin(self, pin: Dict):
        """ Configure and initialize a ADC IO pin.
            See pin object for 'pin' dictionary structure
            'port' is ignored becuase the's only one port
            Actually, it's ALL ignored as there's nothing to configure at the pin level
        """
        bit = pin['bit']
        if pin['type'] != 'ADC' or bit not in list(range(0, 8)):
            fatal("Pin misconfigation: {:}".format(pin['name']))

    def read_pin(self, port: int, bit: int, args={}) -> float:
        """ Read analog value from mapped pin. Returns scaled value """
        register = REG_READINGS_BASE + bit
        scale = args.setdefault('scale', 1.0)
        b1, b0 = self.bus.read_i2c_block_data(self.addr, register, 2)
        value = ((b1 << 4) + (b0 >> 4)) / 4096  # normalize the 12 bit value to 1.0
        if scale == 'vref':
            scale = self.vref
        return value * scale

    def write_pin(self, port: int, bit: int, bit_value: int, args={}):
        print("Attempt to write to ADC pin")
        return None

    def toggle_pin(self, port: int, bit: int, args={}):
        print("Attempt to toggle ADC pin")
        return None

    # Display functions
    def show_ports(self):
        return

    def show_config(self):
        print("Device:         {:}".format(self.partno))
        print("  Device type:       {:}".format(self.type))
        print("  Device addr:       0x{:02X}".format(self.addr))
        try:
            print("  Configuration:     Ox{:02X}".format(self.bus.read_byte_data(self.addr, REG_CONFIGURATION)))
            print("  Interrupt mask:    Ox{:02X}".format(self.bus.read_byte_data(self.addr, REG_INTERRUPT_MASK)))
            print("  Conversion rate:   Ox{:02X}".format(self.bus.read_byte_data(self.addr, REG_CONVERSION_RATE)))
            print("  Channel disable:   Ox{:02X}".format(self.bus.read_byte_data(self.addr, REG_CHANNEL_DISABLE)))
            print("  Deep shutdown:     Ox{:02X}".format(self.bus.read_byte_data(self.addr, REG_DEEP_SHUTDOWN)))
            print("  Adv configuration: Ox{:02X}".format(self.bus.read_byte_data(self.addr, REG_ADVANCED_CONFIGURATION)))
        except IOError as err:
            print("Failed to read configs {:} err {:}".format(self.addr, err))


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute device_adc128d818 class definition - EXITING")
