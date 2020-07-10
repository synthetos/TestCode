""" main.py

    Entry point for tester

"""
from typing import Dict
import time

import qwiic_i2c
from smbus2 import SMBus, i2c_msg

from device_tca9539 import tca9539
from device_tca9539 import CONFIG_DIN_0, CONFIG_DIN_1, CONFIG_DOUT, CONFIG_SPECIALS
from pin import pin


PIN_LED3 = {
    'name': 'led3',
    'type': 'IO',
    'port': 1,
    'bit': 5,
    'direction': 0,
    'polarity': 1,
    'init': 0
}

PIN_LED4 = {
    'name': 'led4',
    'type': 'IO',
    'port': 1,
    'bit': 7,
    'direction': 0,
    'polarity': 1,
    'init': 0
}

PIN_BUTTON4 = {
    'name': 'button4',
    'type': 'IO',
    'port': 1,
    'bit': 6,
    'direction': 1,
    'polarity': 0,
}

def main():

    bus = SMBus(1)
    # din0 = tca9539(bus, CONFIG_DIN_0)
    # din1 = tca9539(bus, CONFIG_DIN_1)
    # dout = tca9539(bus, CONFIG_DOUT)
    specials = tca9539(bus, CONFIG_SPECIALS)

    led3 = pin(specials, PIN_LED3)
    led4 = pin(specials, PIN_LED4)
    but4 = pin(specials, PIN_BUTTON4) 

    specials.show_config()
    specials.show_ports()
    while True:
        led4.toggle()
        time.sleep(1.0)

    while True:
        b = but4.read()
        if b == 1:
            led4.set()
        else:
            led4.clear()
        time.sleep(0.05)

    while True:
        led4.set()
        print("SET")
        time.sleep(1.0)

        led4.clear()
        print("CLEAR")
        time.sleep(1.0)

    bus.close()

# Do Not Delete
if __name__ == "__main__":
    main()
