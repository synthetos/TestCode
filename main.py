""" main.py

    Entry point for tester

"""
import sys
import time
from typing import Dict

# import qwiic_i2c
from smbus2 import SMBus, i2c_msg

from device_wrangler import devices
from pin_wrangler import pins
from pin import pin

# from device_tca9539 import tca9539
# from device_adc128d818 import adc128d818
# from device_dac5574 import dac5574



def main():

    d = devices()
    p = pins(d)

    '''
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
    '''

# Do Not Delete
if __name__ == "__main__":
    main()
