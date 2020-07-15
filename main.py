""" main.py

    Entry point for tester

"""
import time
from typing import Dict

from device_assignments import DEVICE_ASSIGNMENTS
from device_wrangler import devices
from pin_assignments import PIN_ASSIGNMENTS
from pin_wrangler import pins
from pin import pin

from dut_power import dut_power


def main():

    d = devices(DEVICE_ASSIGNMENTS)
    p = pins(d, PIN_ASSIGNMENTS)

    dut = dut_power(p)
    dut.power_on()

    dac_value = 0.0
    while True:
        p.led4.toggle()
        print(p.adc0.read())

        dac_value += 0.005
        p.dac0.write(dac_value)

        time.sleep(0.1)

    while True:
        b = p.but4.read()
        if b == 1:
            p.led4.set()
        else:
            p.led4.clear()
        time.sleep(0.05)

    while True:
        p.led4.set()
        print("SET")
        time.sleep(1.0)

        p.led4.clear()
        print("CLEAR")
        time.sleep(1.0)


# Do Not Delete
if __name__ == "__main__":
    main()
