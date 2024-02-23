import network
import espnow
from machine import Pin
from time import sleep_ms

sta = network.WLAN(network.STA_IF)
sta.active(True)
# sta.disconnect()   # Because ESP8266 auto-connects to last Access Point (Just for ESP8266 Chips)

esp = espnow.ESPNow()
esp.active(True)

led = Pin(18, Pin.OUT)

# main loop
while True:
    host, msg_bytes = esp.recv()
    msg = msg_bytes.decode('utf-8')

    if msg == "ledOn":
        led.on()
        print(host, msg)

    elif msg == "ledOff":
        led.off()
        print(host, msg)

    sleep_ms(100)
