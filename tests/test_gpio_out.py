#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test GPIO out

Usage:
  test_gpio_out.py <pin>

Options:
  -h --help     Show this screen.
  <pin>         Pin number 0 <= PIN <= 26
"""

from time import sleep

import RPi.GPIO as GPIO
from docopt import docopt

args = docopt(__doc__)
PIN = int(args.get("<pin>"))
assert 0 <= PIN <= 26

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# set a port/pin as an output
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, GPIO.HIGH)
sleep(1)
GPIO.output(PIN, GPIO.LOW)

GPIO.cleanup()
