from home_pi.dht import DHT11
import time

PIN = 17

# Start the tempreture sensor
instance = DHT11(pin=PIN)

# Waity 3s for init
print("Wait 3s...")
time.sleep(3)

# Read the sensor
result = instance.read()

# Check if the result is valid
if result.is_valid():
    # Display values
    print("Temperature: %-3.1f C" % result.temperature)
    print("Humidity: %-3.1f %%" % result.humidity)

# Stop the sensor
instance.stop()