""" Run this in order to test serial communication on a computer(Pi4) """

import time
import serial


# Change this to your serial port
serial_port = ['/dev/cu.usbmodem143301', 9600]
# Delay is in seconds
DELAY = 1


def read_write_to_serial_loop():
    """ Sends a random ASCII character/reads to/from the serial port every 'delay' seconds """
    ser = serial.Serial(serial_port[0], serial_port[1], timeout=None)
    time.sleep(1)

    counter = 32

    while True:
        if ser.inWaiting() > 0:
            print(ser.readline(ser.inWaiting()))
        else:
            ser.write(chr(counter).encode('utf-8'))
            counter += 1
            time.sleep(DELAY)

    if counter < 255:
        counter = 32


if __name__ == '__main__':
    read_write_to_serial_loop()
