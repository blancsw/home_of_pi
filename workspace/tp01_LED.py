from gpiozero import PWMLED
from time import sleep

# Start the GPIO 17 as an output
led = PWMLED(17)

led.value = 1.0
sleep(1)
