import network
import espnow
from machine import Pin

sta = network.WLAN(network.STA_IF)
sta.active(True)
# sta.disconnect()   # Because ESP8266 auto-connects to last Access Point (Just for ESP8266 Chips)

esp = espnow.ESPNow()
esp.active(True)