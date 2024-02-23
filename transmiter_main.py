import network
import espnow
from machine import Pin
from time import sleep_ms


sta = network.WLAN(network.STA_IF)
sta.active(True)
# sta.disconnect()      # For ESP8266

esp = espnow.ESPNow()
esp.active(True)

peer = "Replace the receiver MAC address here"  # MAC address of peer's wifi interface
esp.add_peer(peer)  # Must add_peer() before send()

button_pin = Pin(5, Pin.IN, Pin.PULL_UP)


debounce_delay = 50  # Adjust this value to your needs (milliseconds)
last_button_state = 1  # Assuming the button is not pressed initially

# main loop
while True:
    current_button_state = button_pin.value()  # Read the current state of the button

    if (current_button_state != last_button_state):  # Check if the button state has changed
        sleep_ms(debounce_delay)  # Wait for a short time to debounce the button
        current_button_state = (button_pin.value())  # Read the button state again to make sure it's stable

        if (current_button_state != last_button_state):  # If the button state is still different, it's a valid press
            if current_button_state == 0:
                message = b"ledOn"
                print(f"Sending command : {message}")
                esp.send(peer, message)
            else:
                message = b"ledOff"
                print(f"Sending command : {message}")
                esp.send(peer, message)

        last_button_state = current_button_state  # Update the last button state
    
    sleep_ms(100)
