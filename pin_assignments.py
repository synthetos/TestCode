""" pin_assignments.py

    Assign pins and pin properties
    This file can ultimately be replaced with an external YAML file
    See first occurrence of each type for setup details

"""

PIN_ASSIGNMENTS = {

    'din0': {
        'type': 'IO',           # one of IO, ADC, DAC 
        'device': 'digital_0',  # digital IO expander 0 (1 of 3:   i.e. 0, 1, 2)
        'port': 0,              # port 0 or 1
        'bit': 0,               # bits 0 - 7
        'direction': 0,         # 0=output, 1=input
        'polarity': 1,          # 0=non-inverted, 1=inverted
        'init': 0               # initial value on reset (outputs only)
    },

    'led3': {
        'type': 'IO',
        'device': 'control',
        'port': 1,
        'bit': 5,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'led4': {
        'type': 'IO',
        'device': 'control',
        'port': 1,
        'bit': 7,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'button4': {
        'type': 'IO',
        'device': 'control',
        'port': 1,
        'bit': 6,
        'direction': 1,
        'polarity': 0,
    },
    'adc0': {
        'type': 'ADC',
        'device': 'analog_in0',
        'bit': 0,
    },
    'dac0': {
        'type': 'DAC',
        'device': 'analog_out1',
        'bit': 0,
    },
}

# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute pin_assigmnents - EXITING")
