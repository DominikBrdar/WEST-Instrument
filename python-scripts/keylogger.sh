#! /bin/bash

# Program is implemented using Python 3.*
# Python script uses packages pyserial and pynput
# install using pip
pip install pyserial
pip install pynput

# xvfb server
xhost +

# run python script
sudo python3 ./keylogger.py


