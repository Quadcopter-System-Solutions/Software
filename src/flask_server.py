""" Server between Pi (Flask) and controller """

from flask import Flask
from flask_cors import CORS
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    """ Hello World """
    return 'Hello, World!'


@app.route('/zmq/test')
def test_zmq():
    """ Tests to ZMQ server """
    try:
        for request in range(10):
            socket.send(b"test%d" % (request))
            socket.recv()
        return 'Successful test', 200
    # pylint: disable=W0703
    except Exception as error:
        return 'Failed test\nError:\n' + str(error), 500


@app.route('/controls/up/<float:num>')
def controls_up(num):
    """ Goes up by num amount """
    return '%f' % num


@app.route('/controls/down/<float:num>')
def controls_down(num):
    """ Goes up by num amount """
    return '%f' % num
