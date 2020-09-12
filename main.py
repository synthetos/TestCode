""" main.py

    Entry point for tester

"""
import time
from typing import Dict

from device_assignments import DEVICE_ASSIGNMENTS
from device_wrangler import devices
from pin_assignments import PIN_ASSIGNMENTS
from pin_wrangler import pins
from util import reset
from pin import pin

from dut_power import dut_power


def main():

    reset()
    d = devices(DEVICE_ASSIGNMENTS)
    p = pins(d, PIN_ASSIGNMENTS)

    dut = dut_power(p)
    dut.power_on()
    dut.show()

    dac_value = 1.28
    p.dac0.write(dac_value)
    p.dac1.write(dac_value)
    p.dac2.write(dac_value)
    p.dac3.write(dac_value)

    # while True:
    for i in range(0, 5):
        p.dout0.toggle()
        p.dout1.toggle()
        p.led4.toggle()

        dac_value += 0.1
        if dac_value > 3.3:
            dac_value = 0.0
        p.dac0.write(dac_value)

        print("din0: {:}, adc0: {:6.4f}, dac0 {:4.3f}".format(
            p.din1.read(),
            p.adc0.read(),
            dac_value))
        time.sleep(1.0)

    reset()

# Do Not Delete
if __name__ == "__main__":
    main()

"""
    while True:
        # p.led4.toggle()
        # dac_value += 0.005
        # p.dac0.write(dac_value)
        # print(p.adc0.read())

        # dut.clear_alarm()
        dut.power_on()
        dut.show()
        p.led4.set()
        time.sleep(4.0)

        dut.power_off()
        dut.show()
        p.led4.clear()
        time.sleep(4.0)

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
"""