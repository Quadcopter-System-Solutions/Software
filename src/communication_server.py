""" Server between Pi (Flask) and STM32 """

import time
import zmq
import serial

SERIAL = False
ZMQ = True

serial_port = ['/dev/cu.usbmodem143301', 9600]
DELAY = 1

ZMQ_SERVER = "tcp://*:5555"


def start_coms():
    """ Sends a random ASCII character/reads to/from the serial port every 'delay' seconds """
    # Serial
    if SERIAL:
        ser = serial.Serial(serial_port[0], serial_port[1], timeout=None)
        time.sleep(1)
        counter = 32

    # zmq
    if ZMQ:
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind(ZMQ_SERVER)

    while True:
        # Serial
        if SERIAL:
            if ser.inWaiting() > 0:
                print(ser.readline(ser.inWaiting()))
            else:
                ser.write(chr(counter).encode('utf-8'))
                counter += 1
                time.sleep(DELAY)

            if counter < 255:
                counter = 32

        # zmq
        if ZMQ:
            message = socket.recv()
            print("Received request: %s" % message)
            socket.send(b"World")


if __name__ == '__main__':
    start_coms()
