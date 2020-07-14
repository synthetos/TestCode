""" device_assignments.py

    This file can ultimately be supplemented with an external YAML file
    NB: Python 3 preserves ordering in dictionaries - should this ever become important here.

"""

from device_tca9539 import tca9539
from device_adc128d818 import adc128d818
from device_dac5574 import dac5574

DEVICE_ASSIGNMENTS = {
    'digital_0': {
        'comment': 'IO expander for digital inputs 0-15',
        'device': tca9539,          # this is the class for the device
        'addr': 0x74,               # FYI: 116 decimal
    },
    'digital_1': {
        'comment': 'IO expander for digital inputs 16-31',
        'device': tca9539,
        'addr': 0x75,               # FYI: 117 decimal
    },
    'digital_2': {
        'comment': 'IO expander for digital outputs 0-15',
        'device': tca9539,
        'addr': 0x76,               # FYI: 118 decimal
    },
    'control': {
        'comment': 'IO expander for control signals',
        'device': tca9539,
        'addr': 0x77,               # FYI: 119 decimal
    },
    'analog_in0': {
        'comment': 'ADC for analog inputs 0-7 (no interrutps yet)',
        'device': adc128d818,
        'addr': 0x1D,               # FYI: 29 decimal
        'configuration': 0x01,      # 0x01 enables conversion
        'interrupt_mask': 0xFF,     # 0xFF disables all interrupts (for now)
        'conversion_rate': 0x01,    # 0x01 is continuous conversion
        'channel_disable': 0x00,    # 0x00 does not disable any channels
        'deep_shutdown': 0x00,      # 0x00 does not ask for deep shutdown
        'advanced_configuration': 0x02  # 0x02 = Mode 1, internal reference (use 0x03 for ext ref)
    },
    'analog_in1': {
        'comment': 'ADC for analog inputs 8-15',
        'device': adc128d818,
        'addr': 0x1F,               # FYI: 31 decimal
        'configuration': 0x01,      # 0x01 enables conversion
        'interrupt_mask': 0xFF,     # 0xFF disables all interrupts (for now)
        'conversion_rate': 0x01,    # 0x01 is continuous conversion
        'channel_disable': 0x00,    # 0x00 does not disable any channels
        'deep_shutdown': 0x00,      # 0x00 does not ask for deep shutdown
        'advanced_configuration': 0x02  # 0x02 = Mode 1, internal reference (use 0x03 for ext ref)
    },
    'analog_out0': {
        'comment': 'DAC for analog outputs: chA=DAC_1, B=3, C=0 D=DUT_LIMIT_VOLTAGE',
        'device': dac5574,
        'addr': 0x4C,           # FYI: 76 decimal
    },
    'analog_out1': {
        'comment': 'DAC for analog outputs A=2, B=5, C=4, D=no_connect',
        'device': dac5574,
        'addr': 0x4D,           # FYI: 77 decimal
    }
}


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute device_assignments file - EXITING")
