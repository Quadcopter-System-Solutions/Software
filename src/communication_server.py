""" Multithreaded server between Pi (Flask) and STM32 """

import time
import zmq
import serial
from multi_thread import MultiThread

# Flags for multithreads
SERIAL = False
ZMQ = True

# Ports for serial
serial_port = ['/dev/cu.usbmodem143301', 9600]
DELAY = 1

ZMQ_SERVER = "tcp://*:5555"

multi_thread = MultiThread()


def init():
    """ Creates threads for serial and zmq server """
    multi_thread.create_thread(
        function=serial_server,
        name='serial',
    )
    multi_thread.create_thread(
        function=zmq_server,
        name='zmq',
    )


def serial_server():
    """ Sends an ASCII character/reads to/from the serial port every 'delay' seconds """
    ser = serial.Serial(serial_port[0], serial_port[1], timeout=None)
    time.sleep(1)
    counter = 32
    counter = 0

    while True:
        if ser.inWaiting() > 0:
            print(ser.readline(ser.inWaiting()))
        else:
            ser.write(chr(counter).encode('utf-8'))
            counter += 1
            time.sleep(DELAY)

        if counter > 255:
            counter = 32


def zmq_server():
    """ The ZMQ Server prints out messages recieved and returns 'World' """
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(ZMQ_SERVER)

    while True:
        message = socket.recv()
        print("Received request: %s" % message)
        socket.send(b"World")


if __name__ == '__main__':
    init()
    if ZMQ:
        multi_thread.get_thread('zmq').start()
    if SERIAL:
        multi_thread.get_thread('serial').start()
