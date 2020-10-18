""" Server ran on Pi for communication between Mobile and Pi """

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def test():
    """ Test Function """
    return 'Hello, World!'

@app.route('/controls/up/<float:num>')
def controls_up(num):
    """ Goes up by num amount """
    return '%f' %num

@app.route('/controls/down/<float:num>')
def controls_down(num):
    """ Goes up by num amount """
    return '%f' %num
