# Quad Squad - Software

Repo for the software running on the Raspberry Pi 4 for the quadcopter

# Requirements
 - Python 3.8
 - Virtual Environment (I use PipEnv)

# Get Started
 1. Run `pipenv install` in root directory
 2. To start the environment `pipenv shell`

 # Flask
 Flask acts as REST server between the controller device and runs on the Pi.

 For this to work on the Pi without internet connection, setup the pi as a waypoint using this [walkthrough]( https://www.raspberrypi.org/documentation/configuration/wireless/access-point-routed.md)

 ## Start Server
 1. Run either command in `/src`
    - `FLASK_APP=flask_server.py FLASK_ENV=development flask run --host=0.0.0.0`
        - for server that needs to be accessed outside of local machine (most likely used)
    - `FLASK_APP=flask_server.py FLASK_ENV=development flask run`
        - for testing on local machine
 
# ZMQ and serial
 A ZMQ server acts as a middle man between the Flask server and serial communication to the STM.

 ## Start Server
 1. Run `python communication_server.py` in `src`

 ### Note
 Currently looking into multithreading ZMQ and Serial

---

## Note
 Serial port on Raspberry Pi 3B+ is `/dev/ttyACM0`

