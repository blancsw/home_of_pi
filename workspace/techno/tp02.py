import time

from gpiozero import PWMLED

from home_pi.dht import DHT11


def step(temperature, humidity, led, led2):
    """
    Args:
        temperature: temperature get from the sensor in "c"
        humidity: humidity get from the sensor in "%"
        led: LED to control
    """
    # Print information
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    led.value = 1
    led2.value = 1
    # TODO a toi de jouer ici !


led2 = PWMLED(24)
led = PWMLED(23)

# --------------------------------
# Ne pas modifier


if __name__ == "__main__":

    instance = DHT11(pin=4)

    # Wait 3s for init
    print("Wait 3s...")
    time.sleep(3)

    try:
        while True:
            result = instance.read()
            if result.is_valid():
                step(result.temperature, result.humidity, led, led2)
            time.sleep(3)

    except KeyboardInterrupt:
        print("Cleanup")
        instance.stop()
