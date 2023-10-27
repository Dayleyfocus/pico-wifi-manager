import os
import time
import sys
import wifi
import digitalio
import board

# List of network names and passwords
networks = [
    ('Network Name 1', 'Network Password 1'),
    ('Network Name 1', 'Network Password 2'),
    # Add more networks as needed
]

# Number of retries for each network
num_retries = 8

# Initialize LED pin
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# LED control functions
def led_on():
    led.value = True

def led_off():
    led.value = False

def led_blink_fast():
    led_on()
    time.sleep(0.2)
    led_off()
    time.sleep(0.2)

def led_blink_slow():
    led_on()
    time.sleep(0.5)
    led_off()
    time.sleep(0.5)

# Function to check if still connected to WiFi
def check_connection(interval=10):
    while True:
        if wifi.radio.ipv4_address:
            print("Still connected to WiFi.")
            led_on()
        else:
            print("Lost WiFi connection. Reconnecting...")
            led_blink_slow()
            connect_to_wifi()
        time.sleep(interval)

# Function to connect to WiFi
def connect_to_wifi():
    for network_name, network_password in networks:
        for i in range(num_retries):
            try:
                print(f"Connecting to WiFi network: {network_name} (Attempt {i+1})")
                led_blink_fast()
                wifi.radio.connect(network_name, network_password)
                print("Connected to WiFi")
                led_on()
                return True
            except Exception as e:
                print(f"Failed to connect to {network_name}.")
                print("Error:\n", str(e))
                led_off()
                time.sleep(2)
    return False

# Main logic
if connect_to_wifi():
    print("MAC addr:", [hex(i) for i in wifi.radio.mac_address])
    print("IP address is", wifi.radio.ipv4_address)
    check_connection()
else:
    print("Failed to connect to any network, aborting.")
    led_off()
    sys.exit()
