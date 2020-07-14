""" dut_power.py

    Controls for DUT power circuit

    Requires the following pins:
    - dut_board_loaded_input            # interlock signal from pogo board
    - dut_power_enable_output           # digital output to enable DUT power
    - dut_current_limit_reset_output    # digital output to reset power afrter limit event
    - dut_current_limit_alert_input     # digital input to signal a current limit alert
    - dut_scaled_voltage_input          # analog input with voltage level
    - dut_scaled_current_input          # analog input with current level
    - dut_current_limit_output          # analog output to set limit current level

ref: https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/
"""

from typing import Callable
# from util import fatal


class dut_power(object):

    def __init__(self, pins: Callable):

        self.dut_board_loaded_input = pins.dut_board_loaded_input
        self.dut_power_enable_output = pins.dut_power_enable_output
        self.dut_current_limit_reset_output = pins.dut_current_limit_reset_output
        self.dut_current_limit_alert_input = pins.dut_current_limit_alert_input
        self.dut_scaled_voltage_input = pins.dut_scaled_voltage_input
        self.dut_scaled_current_input = pins.dut_scaled_current_input
        self.dut_current_limit_output = pins.dut_current_limit_output
        self.reset()
        return

    def reset(self):
        return

    def read(self):
        """ load internal variables from I2C devices """

        return

    def set_voltage(self, voltage: float):
        """ set voltage parameter """
        return

    def set_current_limit(self, current_limit: float):
        """ set current limit parameters """
        return

    def power_on(self):
        """ Turn power on. Obeys DUT_loaded interlock signal """
        return

    def power_off(self):
        """ turn power off """
        return

    def reset_current_limit_alarm(self):
        """ Reset current limit and return power to OFF condition """
        return

    def show_power(self):
        print("DUT Power Management")
        print("  DUT loaded               {:1d}".format(self.dut_board_loaded_input.read()))
        print("  DUT power enable         {:1d}".format(self.dut_power_enable_output.read()))
        print("  DUT voltage              {:2.3f}V".format(self.dut_scaled_voltage_input.read()))
        print("  DUT current              {:2.3f}A".format(self.dut_scaled_voltage_input.read()))
        print("  DUT current limit        {:2,3f}A".format(self.dut_current_limit_output.read()))
        print("  DUT current limit reset  {:1d}".format(self.dut_current_limit_reset_output.read()))


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute device_dac5574 class definition - EXITING")
