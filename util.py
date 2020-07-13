""" util.py

    Some common utilities

"""
import sys
from typing import Dict, Callable


def fatal(message: str):
    """ Common exit for fatal errors. Aids debugging and keeps code clean """
    print("FATAL: {:} - EXITING".format(message))
    sys.exit(1)


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute util.py - EXITING")
