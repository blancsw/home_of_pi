from time import sleep

from gpiozero import PWMLED

# Start the GPIO 17 as an output
led = PWMLED(4)

led.value = 1
sleep(0.25)
