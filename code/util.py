""" util.py

    Pi GPIO and some common utilities

"""
import sys
# from typing import Dict, Callable

import gpiozero as gpio

from logger import get_logger

log = get_logger()

# Why the hell I have to use an 'LED' to configure a pin is beyond me, but...""
RESET = gpio.LED("GPIO5", active_high=False)
INTERRUPT = gpio.LED("GPIO6", active_high=False)


def reset():
    """ Send a reset pulse to the I2C devices on the baseboard """
    RESET.on()
    RESET.off()


def fatal(message: str):
    """ Common exit for fatal errors. Aids debugging and keeps code clean """
    log.critical("FATAL: {:} - EXITING".format(message))
    # ^^^ set a breakpoint here
    sys.exit(-1)


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute util.py - EXITING")
