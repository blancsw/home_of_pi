#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test DHT sensor

Usage:
  test_dht_sensor.py <pin>

Options:
  -h --help     Show this screen.
  <pin>         Pin number 0 <= PIN <= 26
"""

import os
import sys

from docopt import docopt

FOLDER_ABSOLUTE_PATH = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.join(FOLDER_ABSOLUTE_PATH, ".."))

from home_pi.dht import DHT11
import RPi.GPIO as GPIO
import time
import datetime

args = docopt(__doc__)
PIN = int(args.get("<pin>"))
assert 0 <= PIN <= 26

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = DHT11(pin=PIN)

try:
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.datetime.now()))

            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)

        time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()
