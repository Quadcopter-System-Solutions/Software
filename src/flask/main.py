""" Server ran on Pi for communication between Mobile and Pi """

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Test Function """
    return 'Hello, World!'
