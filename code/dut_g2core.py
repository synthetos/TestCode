""" dut_g2core.py

    This file contains all the code that's specific to the device under test

    Expects to see a g2core firmeware of version ____ or later

"""

import sys, serial, glob
import json
import time
# from time import sleep

# from typing import Dict, Callable
# import gpiozero as gpio

SERIAL_TIMEOUT = 1.5        # time to stop listening in seconds
MARLIN_MODE_DELAY = 2.1     # time to delay if Marlin mode is detected


class g2core(object):

    def __init__(self):
        print("Connecting to g2core")
        self.SERIAL_TIMEOUT = SERIAL_TIMEOUT
        self.s = self.open_serial_port()

    def write(self, data):
        self.s.write(data)

    def serial_close(self):
        self.s.close()

    def readlines(self):
        return self.s.readlines()

    def init_dut(self):
        """
        Initialize g2core device under test - 
        send something to ensure board is responding and set JSON mode
        The first write sometimes returns garbage, so senq ENQ to see if it's responding
        Supposed to send back {"ack":true}
        """

        # ENQ style - board must support ENQ protocol, otherwise use old style
        count = 0
        response = {"ack": False}
        while count < 4:
            self.write("\x05")      # send ENQ
            raw = self.s.readline()
            print(raw)
            try:
                response = json.loads(raw)
            except:
                time.sleep(SERIAL_TIMEOUT)

            if "ack" in response and response["ack"] is True:
                break

            count += 1
            if count > 3:
                print("Serial port connected but board not responding to ENQuiry (0x05)")
                print("Exiting")
                sys.exit(1)

        print("Serial port connected: {0}".format(raw))

    def init_tinyg_legacy(self):
        self.write("{\"fb\":null}\n")      # The first write sometimes returns garbage
        r = self.s.readline()
        self.write("{\"fb\":null}\n")      # So do it again
        r = self.s.readline()
        self.write("{\"fb\":null}\n")      # And again
        r = self.s.readline()
        print("Serial port connected: {0}".format(r))            

    def open_serial_port(self): 
        """
        Open port or die trying
        Does not yet handle multiple connected devices
        """
        ports = self.get_serial_ports()
        if len(ports) == 0:
            print("No serial port found or could not open serial port")
            print("Maybe already open in another program like Coolterm")
            print("Exiting")
            sys.exit(1)

        port = ports[0]

        for port in ports:
            try:
                s = serial.Serial(port, 115200, rtscts=1, timeout=self.SERIAL_TIMEOUT)
            except:
                print("Could not open serial port %s " % port)
                print("Maybe already open in another program like Coolterm")
                print("Exiting")
                sys.exit(1)

            if not s.isOpen:
                print("Could not open serial port: {0}".format(s.name))
                sys.exit(1)
            else:
                print("Serial port opened:    {0}".format(s.name))
            return s    

    def get_serial_ports(self):
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            if port.find("Bluetooth") != -1: # Exclude built-in bluetooth ports on OSX
                continue
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result


# Do Not Delete
if __name__ == "__main__":
    print("Tried to execute util.py - EXITING")
