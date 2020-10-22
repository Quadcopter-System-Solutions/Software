""" Server between Pi (Flask) and controller """

from flask import Flask
from flask_cors import CORS
from multi_thread import MultiThread
from serial_communication import SerialCommunication

multi_thread = MultiThread()
# Flags for starting threads
SERIAL = False
TEST = True

# Serial
SERIAL_PORT = ['/dev/cu.usbmodem143301', 9600]
serial_communication = SerialCommunication(serial_port=SERIAL_PORT, delay=1)

# Flask
app = Flask(__name__)
CORS(app)


def init():
    """ Creates threads for serial and zmq server """
    multi_thread.create_test_thread()
    multi_thread.create_thread(
        function=serial_communication.start_serial,
        name='serial',
    )


@app.route('/')
def hello_world():
    """ Hello World """
    return 'hello world', 200


@app.route('/controls/up/<float:num>')
def controls_up(num):
    """ Goes up by num amount """
    return '%f' % num


@app.route('/controls/down/<float:num>')
def controls_down(num):
    """ Goes up by num amount """
    return '%f' % num


if __name__ == "__main__":
    init()
    if TEST:
        multi_thread.get_thread('test').start()
    if SERIAL:
        multi_thread.get_thread('serial').start()

    app.run(port=8100, host='0.0.0.0', debug=True, use_reloader=True)
