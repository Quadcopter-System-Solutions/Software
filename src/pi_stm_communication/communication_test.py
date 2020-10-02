""" Run this in order to test serial communication on a computer(Pi4) """

import time
# import serial

# To test without serial device
import fake_serial as serial

# Change this to your serial port
serial_port = ['/dev/tty.usbmodem1d11', 9600]
# Delay is in seconds
delay = 0.3


def read_write_to_serial_loop():
    """ Sends a random ASCII character/reads to/from the serial port every 'delay' seconds """
    counter = 32
    ser = serial.Serial(serial_port[0], serial_port[1])

    while True:
        ser.write(str(chr(counter)))
        print(ser.read())
        time.sleep(delay)

        counter += 1

        # Resets counter so it doesn't send unreadable ASCII
        if counter == 255:
            counter = 32


if __name__ == '__main__':
    read_write_to_serial_loop()
