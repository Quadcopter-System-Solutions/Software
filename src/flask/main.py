""" Server ran on Pi for communication between Mobile and Pi """

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    """ Test Function """
    return 'Hello, World!'
