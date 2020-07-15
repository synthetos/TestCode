""" pin_assignments.py

    Assign pins and pin properties
    This file can ultimately be replaced with an external YAML file
    See first occurrence of each type for setup details

"""

PIN_ASSIGNMENTS = {

    # 1st tca9539 IO port expander - 16 digital inputs
    'din0': {
        'comment': 'Digital input channel 0',  # comment is optional
        'type': 'IO',           # one of IO, ADC, DAC
        'device': 'digital_0',  # digital IO expander 0 (1 of 3:   i.e. 0, 1, 2)
        'port': 0,              # port 0 or 1
        'bit': 0,               # bits 0 - 7
        'direction': 1,         # 0=output, 1=input
        'polarity': 1,          # 0=non-inverted, 1=inverted
        # 'init': 0               # initial value on reset (outputs only)
    },
    'din1': {
        'comment': 'Digital input channel 1',
        'type': 'IO',
        'device': 'digital_0',
        'port': 0,
        'bit': 1,
        'direction': 1,
        'polarity': 1,
    },
    'din2': {
        'comment': 'Digital input channel 2',
        'type': 'IO',
        'device': 'digital_0',
        'port': 0,
        'bit': 2,
        'direction': 1,
        'polarity': 1,
    },
    'din3': {
        'comment': 'Digital input channel 3',
        'type': 'IO',
        'device': 'digital_0',
        'port': 0,
        'bit': 3,
        'direction': 1,
        'polarity': 1,
    },
    'din4': {
        'comment': 'Digital input channel 4',
        'type': 'IO',
        'device': 'digital_0',
        'port': 0,
        'bit': 4,
        'direction': 1,
        'polarity': 1,
    },
    'din5': {
        'comment': 'Digital input channel 5',
        'type': 'IO',
        'device': 'digital_0',
        'port': 0,
        'bit': 5,
        'direction': 1,
        'polarity': 1,
    },
    'din6': {
        'comment': 'Digital input channel 6',
        'type': 'IO',
        'device': 'digital_0',
        'port': 0,
        'bit': 6,
        'direction': 1,
        'polarity': 1,
    },
    'din7': {
        'comment': 'Digital input channel 7',
        'type': 'IO',
        'device': 'digital_0',
        'port': 0,
        'bit': 7,
        'direction': 1,
        'polarity': 1,
    },
    'din8': {
        'comment': 'Digital input channel 8',
        'type': 'IO',
        'device': 'digital_0',
        'port': 1,
        'bit': 0,
        'direction': 1,
        'polarity': 1,
    },
    'din9': {
        'comment': 'Digital input channel 9',
        'type': 'IO',
        'device': 'digital_0',
        'port': 1,
        'bit': 1,
        'direction': 1,
        'polarity': 1,
    },
    'din10': {
        'comment': 'Digital input channel 10',
        'type': 'IO',
        'device': 'digital_0',
        'port': 1,
        'bit': 2,
        'direction': 1,
        'polarity': 1,
    },
    'din11': {
        'comment': 'Digital input channel 11',
        'type': 'IO',
        'device': 'digital_0',
        'port': 1,
        'bit': 3,
        'direction': 1,
        'polarity': 1,
    },
    'din12': {
        'comment': 'Digital input channel 12',
        'type': 'IO',
        'device': 'digital_0',
        'port': 1,
        'bit': 4,
        'direction': 1,
        'polarity': 1,
    },
    'din13': {
        'comment': 'Digital input channel 13',
        'type': 'IO',
        'device': 'digital_0',
        'port': 1,
        'bit': 5,
        'direction': 1,
        'polarity': 1,
    },
    'din14': {
        'comment': 'Digital input channel 14',
        'type': 'IO',
        'device': 'digital_0',
        'port': 1,
        'bit': 6,
        'direction': 1,
        'polarity': 1,
    },
    'din15': {
        'comment': 'Digital input channel 15',
        'type': 'IO',
        'device': 'digital_0',
        'port': 1,
        'bit': 7,
        'direction': 1,
        'polarity': 1,
    },

    # 2nd tca9539 IO port expander - 16 digital inputs
    'din16': {
        'comment': 'Digital input channel 16',
        'type': 'IO',
        'device': 'digital_1',
        'port': 0,
        'bit': 0,
        'direction': 1,
        'polarity': 1,
    },
    'din17': {
        'comment': 'Digital input channel 17',
        'type': 'IO',
        'device': 'digital_1',
        'port': 0,
        'bit': 1,
        'direction': 1,
        'polarity': 1,
    },
    'din18': {
        'comment': 'Digital input channel 18',
        'type': 'IO',
        'device': 'digital_1',
        'port': 0,
        'bit': 2,
        'direction': 1,
        'polarity': 1,
    },
    'din19': {
        'comment': 'Digital input channel 19',
        'type': 'IO',
        'device': 'digital_1',
        'port': 0,
        'bit': 3,
        'direction': 1,
        'polarity': 1,
    },
    'din20': {
        'comment': 'Digital input channel 20',
        'type': 'IO',
        'device': 'digital_1',
        'port': 0,
        'bit': 4,
        'direction': 1,
        'polarity': 1,
    },
    'din21': {
        'comment': 'Digital input channel 21',
        'type': 'IO',
        'device': 'digital_1',
        'port': 0,
        'bit': 5,
        'direction': 1,
        'polarity': 1,
    },
    'din22': {
        'comment': 'Digital input channel 22',
        'type': 'IO',
        'device': 'digital_1',
        'port': 0,
        'bit': 6,
        'direction': 1,
        'polarity': 1,
    },
    'din23': {
        'comment': 'Digital input channel 23',
        'type': 'IO',
        'device': 'digital_1',
        'port': 0,
        'bit': 7,
        'direction': 1,
        'polarity': 1,
    },
    'din24': {
        'comment': 'Digital input channel 24',
        'type': 'IO',
        'device': 'digital_1',
        'port': 1,
        'bit': 0,
        'direction': 1,
        'polarity': 1,
    },
    'din25': {
        'comment': 'Digital input channel 25',
        'type': 'IO',
        'device': 'digital_1',
        'port': 1,
        'bit': 1,
        'direction': 1,
        'polarity': 1,
    },
    'din26': {
        'comment': 'Digital input channel 26',
        'type': 'IO',
        'device': 'digital_1',
        'port': 1,
        'bit': 2,
        'direction': 1,
        'polarity': 1,
    },
    'din27': {
        'comment': 'Digital input channel 27',
        'type': 'IO',
        'device': 'digital_1',
        'port': 1,
        'bit': 3,
        'direction': 1,
        'polarity': 1,
    },
    'din28': {
        'comment': 'Digital input channel 28',
        'type': 'IO',
        'device': 'digital_1',
        'port': 1,
        'bit': 4,
        'direction': 1,
        'polarity': 1,
    },
    'din29': {
        'comment': 'Digital input channel 29',
        'type': 'IO',
        'device': 'digital_1',
        'port': 1,
        'bit': 5,
        'direction': 1,
        'polarity': 1,
    },
    'din30': {
        'comment': 'Digital input channel 30',
        'type': 'IO',
        'device': 'digital_1',
        'port': 1,
        'bit': 6,
        'direction': 1,
        'polarity': 1,
    },
    'din31': {
        'comment': 'Digital input channel 31',
        'type': 'IO',
        'device': 'digital_1',
        'port': 1,
        'bit': 7,
        'direction': 1,
        'polarity': 1,
    },

    # 3rd tca9539 IO port expander - 16 digital outputs
    'dout0': {
        'comment': 'Digital output channel 0',
        'type': 'IO',
        'device': 'digital_2',
        'port': 0,
        'bit': 0,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout1': {
        'comment': 'Digital output channel 1',
        'type': 'IO',
        'device': 'digital_2',
        'port': 0,
        'bit': 1,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout2': {
        'comment': 'Digital output channel 2',
        'type': 'IO',
        'device': 'digital_2',
        'port': 0,
        'bit': 2,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout3': {
        'comment': 'Digital output channel 3',
        'type': 'IO',
        'device': 'digital_2',
        'port': 0,
        'bit': 3,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout4': {
        'comment': 'Digital output channel 4',
        'type': 'IO',
        'device': 'digital_2',
        'port': 0,
        'bit': 4,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout5': {
        'comment': 'Digital output channel 5',
        'type': 'IO',
        'device': 'digital_2',
        'port': 0,
        'bit': 5,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout6': {
        'comment': 'Digital output channel 6',
        'type': 'IO',
        'device': 'digital_2',
        'port': 0,
        'bit': 6,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout7': {
        'comment': 'Digital output channel 7',
        'type': 'IO',
        'device': 'digital_2',
        'port': 0,
        'bit': 7,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout8': {
        'comment': 'Digital output channel 8',
        'type': 'IO',
        'device': 'digital_2',
        'port': 1,
        'bit': 0,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout9': {
        'comment': 'Digital output channel 9',
        'type': 'IO',
        'device': 'digital_2',
        'port': 1,
        'bit': 1,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout10': {
        'comment': 'Digital output channel 10',
        'type': 'IO',
        'device': 'digital_2',
        'port': 1,
        'bit': 2,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout11': {
        'comment': 'Digital output channel 11',
        'type': 'IO',
        'device': 'digital_2',
        'port': 1,
        'bit': 3,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout12': {
        'comment': 'Digital output channel 12',
        'type': 'IO',
        'device': 'digital_2',
        'port': 1,
        'bit': 4,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout13': {
        'comment': 'Digital output channel 13',
        'type': 'IO',
        'device': 'digital_2',
        'port': 1,
        'bit': 5,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout14': {
        'comment': 'Digital output channel 14',
        'type': 'IO',
        'device': 'digital_2',
        'port': 1,
        'bit': 6,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dout15': {
        'comment': 'Digital output channel 15',
        'type': 'IO',
        'device': 'digital_2',
        'port': 1,
        'bit': 7,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },

    # 4th tca9539 IO port expander - 16 digital outputs
    'nc_0': {  # channel 0 - not connected
        'comment': 'Digital control bit 0 - intentionally not connected',
        'type': 'IO',
        'device': 'control',
        'port': 0,
        'bit': 0,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'dut_power_enable_output': {  # channel 1
        'comment': 'DUT power enable',
        'type': 'IO',
        'device': 'control',
        'port': 0,
        'bit': 1,
        'direction': 0,
        'polarity': 0,  # non-inverted: set() to enable
        'init': 0
    },
    'dut_current_limit_reset_output': {  # channel 2
        'comment': 'DUT current limit reset',
        'type': 'IO',
        'device': 'control',
        'port': 0,
        'bit': 2,
        'direction': 0,
        'polarity': 0,  # non-inverted: set() selects latched ALERT mode
        'init': 0
    },
    'dut_current_limit_alert_input': {  # channel 3
        'comment': 'DUT current limit alert',
        'type': 'IO',
        'device': 'control',
        'port': 0,
        'bit': 3,
        'direction': 1,
        'polarity': 1,  # inverted: Over-current ALERT drives pin HIGH 
        'init': 0
    },
    'dut_board_loaded_input': {  # channel 4
        'comment': 'DUT loaded interlock signal from pogo board',
        'type': 'IO',
        'device': 'control',
        'port': 0,
        'bit': 4,
        'direction': 1,
        'polarity': 1,
        'init': 0
    },
    'control_uncommitted_0': {  # channel 5
        'comment': 'Uncommitted control bit 0',
        'type': 'IO',
        'device': 'control',
        'port': 0,
        'bit': 5,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'control_uncommitted_1': {  # channel 6
        'comment': 'Uncommitted control bit 1',
        'type': 'IO',
        'device': 'control',
        'port': 0,
        'bit': 6,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'nc_7': {  # channel 7 - not connected
        'comment': 'Digital control bit 7 - intentionally not connected',
        'type': 'IO',
        'device': 'control',
        'port': 0,
        'bit': 7,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'button1': {  # channel 8
        'type': 'IO',
        'device': 'control',
        'port': 1,
        'bit': 0,
        'direction': 1,
        'polarity': 1,
    },
    'led1': {  # channel 9
        'type': 'IO',
        'device': 'control',
        'port': 1,
        'bit': 1,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'button2': {  # channel 10
        'type': 'IO',
        'device': 'control',
        'port': 1,
        'bit': 2,
        'direction': 1,
        'polarity': 1,
    },
    'led2': {  # channel 11
        'type': 'IO',
        'device': 'control',
        'port': 1,
        'bit': 3,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'button3': {  # channel 12
        'type': 'IO',
        'device': 'control',
        'port': 1,
        'bit': 4,
        'direction': 1,
        'polarity': 1,
    },
    'led3': {  # channel 13
        'type': 'IO',
        'device': 'control',
        'port': 1,
        'bit': 5,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },
    'button4': {  # channel 14
        'type': 'IO',
        'device': 'control',
        'port': 1,
        'bit': 6,
        'direction': 1,
        'polarity': 1,
    },
    'led4': {  # channel 15
        'type': 'IO',
        'device': 'control',
        'port': 1,
        'bit': 7,
        'direction': 0,
        'polarity': 1,
        'init': 0
    },

    # #########################
    # ### Analog Input Pins ###
    # #########################

    # 1st adc128d818 Analog to Digital converter - 8 analog inputs
    'adc0': {                       # Configuration for ADCs
        'type': 'ADC',              # Type must be 'ADC'
        'device': 'analog_in0',     # name of device hosting pin
        'bit': 0,                   # input channel
        'scale': 'vref'             # full scale input returns: Vref (i.e. returns input volts)
        # 'scale': 1.0              # full scale input returns: 1.0 (by way of example)
        # 'scale': 100.0            # full scale input returns: 100 (by way of example)
    },
    'adc1': {
        'type': 'ADC',
        'device': 'analog_in0',
        'bit': 1,
        'scale': 'vref'
    },
    'adc2': {
        'type': 'ADC',
        'device': 'analog_in0',
        'bit': 2,
        'scale': 'vref'
    },
    'adc3': {
        'type': 'ADC',
        'device': 'analog_in0',
        'bit': 3,
        'scale': 'vref'
    },
    'adc4': {
        'type': 'ADC',
        'device': 'analog_in0',
        'bit': 4,
        'scale': 'vref'
    },
    'adc5': {
        'type': 'ADC',
        'device': 'analog_in0',
        'bit': 5,
        'scale': 'vref'
    },
    'adc6': {
        'type': 'ADC',
        'device': 'analog_in0',
        'bit': 6,
        'scale': 'vref'
    },
    'adc7': {
        'type': 'ADC',
        'device': 'analog_in0',
        'bit': 7,
        'scale': 'vref'
    },
    # 2nd adc128d818 Analog to Digital converter - 8 analog inputs
    'adc8': {
        'type': 'ADC',
        'device': 'analog_in1',
        'bit': 0,
        'scale': 'vref'
    },
    'adc9': {
        'type': 'ADC',
        'device': 'analog_in1',
        'bit': 1,
        'scale': 'vref'
    },
    'adc10': {
        'type': 'ADC',
        'device': 'analog_in1',
        'bit': 2,
        'scale': 'vref'
    },
    'adc11': {
        'type': 'ADC',
        'device': 'analog_in1',
        'bit': 3,
        'scale': 'vref'
    },
    'adc12': {
        'type': 'ADC',
        'device': 'analog_in1',
        'bit': 4,
        'scale': 'vref'
    },
    'adc13': {
        'type': 'ADC',
        'device': 'analog_in1',
        'bit': 5,
        'scale': 'vref'
    },
    'dut_scaled_voltage_input': {
        'comment': 'DUT scaled voltage input',
        'type': 'ADC',
        'device': 'analog_in1',
        'bit': 6,
        'scale': 'vref'
    },
    'dut_scaled_current_input': {
        'comment': 'DUT scaled current input',
        'type': 'ADC',
        'device': 'analog_in1',
        'bit': 7,
        'scale': 'vref'
    },

    # ##########################
    # ### Analog Output Pins ###
    # ##########################

    # 1st dac5574 Digital to Analog converter - 4 analog outputs
    'dac1': {                       # 0x4C, Vout A
        'comment': 'DAC channel 1',  # optional
        'type': 'DAC',              # must be 'DAC'
        'device': 'analog_out0',    # name of device hosting pin
        'bit': 0,                   # output channel
        'scale': 3.3                # value for full scale output
    },
    'dac3': {                       # 0x4C, Vout B
        'comment': 'DAC channel 3',
        'type': 'DAC',
        'device': 'analog_out0',
        'bit': 1,
        'scale': 3.3
    },
    'dac0': {                       # 0x4C, Vout C
        'comment': 'DAC channel 0',
        'type': 'DAC',
        'device': 'analog_out0',
        'bit': 2,
        'scale': 3.3
    },
    'dut_current_limit_output': {   # 0x4C, Vout D
        'comment': 'DUT current limit output',
        'type': 'DAC',
        'device': 'analog_out0',
        'bit': 3,
        'scale': 16.5  # normalizes set(n) current limit to Amps
    },

    # 2nd dac5574 Digital to Analog converter - 4 analog outputs
    'dac2': {                       # 0x4F, Vout A
        'comment': 'DAC channel 2',
        'type': 'DAC',
        'device': 'analog_out1',
        'bit': 0,
        'scale': 3.3
    },
    'dac5': {                       # 0x4F, Vout B
        'comment': 'DAC channel 5',
        'type': 'DAC',
        'device': 'analog_out1',
        'bit': 1,
        'scale': 3.3
    },
    'dac4': {                       # 0x4F, Vout C
        'comment': 'DAC channel 4',
        'type': 'DAC',
        'device': 'analog_out1',
        'bit': 2,
        'scale': 3.3
    },
    'dac_nc': {                     # 0x4F, Vout D
        'comment': 'DAC channel intentionally not connected',
        'type': 'DAC',
        'device': 'analog_out1',
        'bit': 3,
        'scale': 3.3
    },

}

# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute pin_assigmnents - EXITING")
