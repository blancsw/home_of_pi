#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from home_pi.motor_hat import MotorDriver

print("this is a motor driver test code")
motor = MotorDriver()

print("forward 2 s")
motor.motor_run(0, 'forward', 100)
motor.motor_run(1, 'forward', 100)
time.sleep(2)

print("backward 2 s")
motor.motor_run(0, 'backward', 100)
motor.motor_run(1, 'backward', 100)
time.sleep(2)

print("stop")
motor.motor_stop(0)
motor.motor_stop(1)
