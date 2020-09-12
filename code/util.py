""" util.py

    Pi GPIO and some common utilities

"""
import sys
from typing import Dict, Callable

import gpiozero as gpio

# Why the fuck I have to use an 'LED' to configure a pin is beyond me, but...""
RESET = gpio.LED("GPIO5", active_high=False)
INTERRUPT = gpio.LED("GPIO6", active_high=False)


def reset():
    RESET.on()
    RESET.off()


def fatal(message: str):
    """ Common exit for fatal errors. Aids debugging and keeps code clean """
    print("FATAL: {:} - EXITING".format(message))
    sys.exit(1)


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute util.py - EXITING")
