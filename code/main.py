""" main.py

    Entry point for tester

toDo:
- make devices and pin wrnaglers work more like test wrangler. Called explicitly
"""

import os
import time
# from typing import Dict

from device_assignments import DEVICE_ASSIGNMENTS
from device_wrangler import devices
from pin_assignments import PIN_ASSIGNMENTS
from pin_wrangler import pins
from test_wrangler import test_wrangler
# from test_sequencer import test_sequence
from dut_power import dut_power
from util import reset
from logger import get_logger

# os.chdir('./TestCode')
# os.chdir('.')
log = get_logger()


def main():

    reset()
    dev = devices(DEVICE_ASSIGNMENTS)
    pin = pins(dev, PIN_ASSIGNMENTS)
    tests = test_wrangler(pin, {"no_dut_yet": None}, "no_test_file_yet")
    test_gen = tests.test_sequence_generator()

    dut = dut_power(pin)
    dut.power_on()
    dut.show()

    dac_value = 1.28
    pin.dac0.write(dac_value)
    pin.dac1.write(dac_value)
    pin.dac2.write(dac_value)
    pin.dac3.write(dac_value)

    for i in range(0, 5):
        pin.dout0.toggle()
        pin.dout1.toggle()
        pin.led4.toggle()

        dac_value += 0.1
        if dac_value > 3.3:
            dac_value = 0.0
        pin.dac0.write(dac_value)

        print("din0: {:}, adc0: {:6.4f}, dac0 {:4.3f}".format(
            pin.din1.read(),
            pin.adc0.read(),
            dac_value))
        time.sleep(1.0)

    while True:
        func, test_obj = next(test_gen)
        if func is None:    # tests are complete
            break

        result = func(test_obj)
        print(result)

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