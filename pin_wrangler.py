""" pin_wrangler.py

    Instantiate pins from pin_assignments
    Requires devices (must run device_wrangler first)

"""
import sys
from typing import Dict

# from smbus2 import SMBus, i2c_msg
from pin_assignments import PIN_ASSIGNMENTS
from pin import pin


class pins(object):

    def __init__(self, devices):

        self.pin = {}
        self.devices = devices

        for name, properties in PIN_ASSIGNMENTS.items():
            device = self.devices.device[properties['device']]
            self.pin[name] = pin(device, properties)



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

    bus.close()
    '''

# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute pin_wrangler class definition - EXITING")
