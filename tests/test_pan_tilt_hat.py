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

FOLDER_ABSOLUTE_PATH = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.join(FOLDER_ABSOLUTE_PATH, ".."))

from home_pi.pan_tilt.pwm import PWM
from home_pi.pan_tilt.servo import Servo

pwm_P1 = Servo(PWM('P0'))
pwm_P0 = Servo(PWM('P1'))

pwm_P1.angle(-45)
