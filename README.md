# Quad Squad - Software

Repo for the software running on the Raspberry Pi 4 for the quadcopter

# Requirements
 - Python 3.8
 - Virtual Environment (I use PipEnv)

# Get Started
 1. Run `pipenv install` in root directory
 2. To start the environment `pipenv shell`


# Multithreaded Server
 ## Flask
 Flask acts as REST server between the controller device and runs on the Pi on the main thread.

 For this to work on the Pi without internet connection, setup the pi as a waypoint using this [walkthrough]( https://www.raspberrypi.org/documentation/configuration/wireless/access-point-routed.md)

 ## Serial Communication
 On another thread, there is a serial communication loop running

# Start Server
 1. 
 2. Run either command in `/src`
    - `python main.py`

### Note
 - Serial port on Raspberry Pi 3B+ is `/dev/ttyACM0`
 - Still need to build logic between serial and STM
