""" logger.py

Setup logging and expose log service
Ref:
    https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook

    # full formatter example from above
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
"""

import os, sys
import time
import logging

from settings import __LOG_DIR, __LOGFILE, __LOGLEVEL

__LOGGER = None  # initial condition for instance hook


def get_logger():  # Lazy loader: Instantiate class into global variable when first called
    global __LOGGER
    if __LOGGER is None:
        __LOGGER = Logger(__LOG_DIR, __LOGFILE, __LOGLEVEL)
    return __LOGGER


class Logger(object):
    def __init__(self, logging_dir: str, basename: str, loglevel=20):

        self.logger = logging.getLogger('tester')
        self.logger.setLevel(logging.INFO)

        # create file handler which logs down to debug messages
        logfile = "{:}-{:}.txt".format(
            basename, time.strftime("%y%m%d-%H%M", time.localtime(time.time())))
        logpath = os.path.join(logging_dir, logfile)
        fh = logging.FileHandler(logpath)
        fh.setLevel(logging.INFO)

        # format = '%(levelname)s - %(message)s'
        format = '%(asctime)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(format)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        # add a console handler with an INFO log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        print("")
        print("---------------------------------------------------------------------------------")
        self.logger.warning("Setup logger")

    def critical(self, logstring):
        self.logger.critical(logstring)

    def error(self, logstring):
        self.logger.error(logstring)

    def warning(self, logstring):
        self.logger.warning(logstring)

    def info(self, logstring):
        self.logger.info(logstring)

    def debug(self, logstring):
        self.logger.debug(logstring)
