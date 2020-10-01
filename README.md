# Quad Squad - Software

Repo for the software running on the Raspberry Pi 4 for the quadcopter

# Requirements
 - Python 3.8
 - Virtual Environment (I use PipEnv)

# Get Started
 1. Run `pipenv install` in root directory
 2. To start the environment `pipenv shell`

# Test Raspberry Pi 4 to Serial
 - With the environment active, in the root directory run `python src/pi_stm_communication/communication_test.py`
 - Or without activating the environment `pipenv run python src/pi_stm_communication/communication_test.py`
 - If testing without a serial device comment out `import serial` and uncomment `import fake_serial as serial`