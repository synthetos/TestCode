""" settings.py

Global settings

This should all be converted to a config file and config manager if you ever
care about configs being able to be editable outside the executable code.
"""

import os

# ### General global settings
__DATA_DIR = os.path.join(os.getcwd(), 'data')
__CONFIG_DIR = os.path.join(os.getcwd(), 'config')
__LOG_DIR = os.path.join(os.getcwd(), 'logs')
__DB_FILE = os.path.join(os.getcwd(), 'db', 'tester.db')

__LOGFILE = 'log'           # filename gets a timestamp added
__LOGLEVEL = 20             # 40 = error, 30 = warning, 20 = info, 10 = debug
__DELAYS = (1, 4)           # Exponential delay: min seconds, max seconds
__CACHEMODE = 'standard'    # 'standard', 'live' or 'cache'

__DATETIME_FORMAT_STR = "%Y-%m-%d %H:%M:%S.%f"

# SCREEN_WIDTH = 2880    # Set for Retina display
# SCREEN_HEIGHT = 1800
SCREEN_WIDTH = 1920     # Adjusted for the reality of what my Retina display shows
SCREEN_HEIGHT = 1200
