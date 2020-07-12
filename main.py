""" main.py

    Entry point for tester

"""
import sys
import time
from typing import Dict

# import qwiic_i2c
from smbus2 import SMBus, i2c_msg

from device_tca9539 import tca9539
from device_tca9539 import CONFIG_DIN_0, CONFIG_DIN_1, CONFIG_DOUT, CONFIG_SPECIALS

from device_adc128d818 import adc128d818, CONFIG_ADC_0  # , CONFIG_ADC_1
from device_dac5574 import dac5574, CONFIG_DAC_1  # , CONFIG_DAC_0

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

PIN_ADC0 = {
    'name': 'adc0',
    'type': 'ADC',
    'bit': 0,
}

PIN_DAC0 = {
    'name': 'dac0',
    'type': 'DAC',
    'bit': 0,
}

def main():

    bus = SMBus(1)
    # din0 = tca9539(bus, CONFIG_DIN_0)
    # din1 = tca9539(bus, CONFIG_DIN_1)
    # dout = tca9539(bus, CONFIG_DOUT)
    specials = tca9539(bus, CONFIG_SPECIALS)

    ain0 = adc128d818(bus, CONFIG_ADC_0)
    ain0.show_config()

    aout1 = dac5574(bus, CONFIG_DAC_1)

    led3 = pin(specials, PIN_LED3)
    led4 = pin(specials, PIN_LED4)
    but4 = pin(specials, PIN_BUTTON4) 
    adc0 = pin(ain0, PIN_ADC0)
    dac0 = pin(aout1, PIN_DAC0)

    specials.show_config()
    specials.show_ports()
    dac_value = 0.0

    while True:
        led4.toggle()
        print(adc0.read())

        dac_value += 0.005
        dac0.write(dac_value)

        time.sleep(0.1)

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
