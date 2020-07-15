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

    'dut_current_limit_output' is used to set the threshold current limit
    The overcurrent ALERT threshold voltage is the voltage drop across the sense resistor.
    Example:
        Iload   5.00    amps (example current limit)
        Rsense  0.01    ohms (this is value of the sense resistor)
        Gain    20.0    gain (this is a fixed internal value of the INA301)
              ------
        Vtrip   1.00    volts to set overcurrent to 5.00 amps
                        (Iload * Rsense * Gain)

        Set DAC dut_current_limit_output 'scale' to 16.5
        This normalizes the set(n) number to amps,
        meaning that the full DAC output (3.3v) would set 16.5 amps

ref: https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/
"""

from typing import Callable, Dict


INITIAL_CURRENT_LIMIT = 0.1  # amps


class dut_power(object):

    def __init__(self, pins: Callable):

        self.board_loaded = pins.dut_board_loaded_input
        self.power_enable = pins.dut_power_enable_output
        self.current_limit_reset = pins.dut_current_limit_reset_output
        self.current_limit_alert = pins.dut_current_limit_alert_input
        self.scaled_voltage = pins.dut_scaled_voltage_input
        self.scaled_current = pins.dut_scaled_current_input
        self.current_limit = pins.dut_current_limit_output
        self.reset()
        return

    def reset(self):
        self.power_enable.clear()            # disable output voltage

        self.current_limit_reset.clear()     # clear any ALERT condition
        self.current_limit_reset.set()       # ...and enable latched mode

        self.current_limit.set(INITIAL_CURRENT_LIMIT)
        return

    def set_current_limit(self, current_limit: float):
        """ set current limit value """
        self.current_limit.set(current_limit)

    def power_on(self):
        """ Turn power on. Obeys DUT_loaded interlock signal """
        self.power_enable.set()

    def power_off(self):
        """ turn power off """
        self.power_enable.clear()

    def reset_current_limit_alarm(self):
        """ Reset current limit and return power to OFF condition """
        return

    def read(self) -> Dict:
        """ Return all values """
        values = {
            'dut_loaded': self.board_loaded.read(),
            'power_enable': self.power_enable.read(),
            'voltage': self.scaled_voltage.read(),
            'current': self.scaled_current.read(),
            'current_limit': self.current_limit.read(),
            'current_limit_alert': self.current_limit_alert.read(),
            'current_limit_reset': self.current_limit_reset.read(),
        }
        return values

    def show_power(self):
        print("DUT Power Management")
        print("  DUT loaded               {:1d}".format(self.board_loaded.read()))
        print("  DUT power enable         {:1d}".format(self.power_enable.read()))
        print("  DUT voltage              {:2.3f}V".format(self.scaled_voltage.read()))
        print("  DUT current              {:2.3f}A".format(self.scaled_current.read()))
        print("  DUT current limit        {:2,3f}A".format(self.current_limit.read()))
        print("  DUT current limit alert  {:1d}".format(self.current_limit_alert.read()))
        print("  DUT current limit reset  {:1d}".format(self.current_limit_reset.read()))


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute dut_power class definition - EXITING")
