""" Anything related serial communication between Pi and STM """

import time
import serial


class SerialCommunication():
    """ Class for handling serial communication """
    def __init__(self, serial_port, delay=1):
        self.serial_port = serial_port
        self.delay = delay

    def start_serial(self):
        """ Sends an ASCII character/reads to/from the serial port every 'delay' seconds """
        ser = serial.Serial(self.serial_port[0], self.serial_port[1], timeout=None)
        time.sleep(1)

        counter = 32

        while True:
            if ser.inWaiting() > 0:
                print(ser.readline(ser.inWaiting()))
            else:
                ser.write(chr(counter).encode('utf-8'))
                counter += 1
                time.sleep(self.delay)

            if counter > 255:
                counter = 32
