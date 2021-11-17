import os
import sys
from home_pi.pan_tilt.pwm import PWM
from home_pi.pan_tilt.servo import Servo

pwm_P1 = Servo(PWM('P0'))
pwm_P0 = Servo(PWM('P1'))

pwm_P1.angle(0)
pwm_P0.angle(0)