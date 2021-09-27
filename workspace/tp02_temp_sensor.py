import time

from gpiozero import PWMLED, LED

from home_pi.dht import DHT11


def step(temperature, humidity, led, fan):
    """
    Args:
        temperature: temperature get from the sensor in "c"
        humidity: humidity get from the sensor in "%"
        led: LED to control
        fan: Fan to control
    """
    # Print information
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    # Turn on the LED
    led.value = 1.0
    fan.on()

    # TODO a toi de jouer ici !


if __name__ == "__main__":
    instance = DHT11(pin=4)
    led = PWMLED(17)
    fan = LED(14)

    # Wait 3s for init
    print("Wait 3s...")
    time.sleep(3)

    try:
        while True:
            result = instance.read()
            if result.is_valid():
                step(result.temperature, result.humidity, led, fan)
            time.sleep(3)

    except KeyboardInterrupt:
        print("Cleanup")
        instance.stop()
