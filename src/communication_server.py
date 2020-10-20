""" Server between Pi (Flask) and STM32 """

import time
import zmq
import serial

serial_port = ['/dev/cu.usbmodem143301', 9600]
DELAY = 1

ZMQ_SERVER = "tcp://*:5555"


def start_coms(serial_flag, zmq_flag):
    """ Sends a random ASCII character/reads to/from the serial port every 'delay' seconds """
    # Serial
    if serial_flag:
        ser = serial.Serial(serial_port[0], serial_port[1], timeout=None)
        time.sleep(1)
        counter = 32

    # zmq
    if zmq_flag:
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind(ZMQ_SERVER)

    while True:
        # Serial
        if serial_flag:
            if ser.inWaiting() > 0:
                print(ser.readline(ser.inWaiting()))
            else:
                ser.write(chr(counter).encode('utf-8'))
                counter += 1
                time.sleep(DELAY)

            if counter < 255:
                counter = 32

        # zmq
        if zmq_flag:
            message = socket.recv()
            print("Received request: %s" % message)
            socket.send(b"World")


if __name__ == '__main__':
    start_coms(serial_flag=False, zmq_flag=True)
