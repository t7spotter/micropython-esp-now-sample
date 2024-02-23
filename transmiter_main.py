import network
import espnow
from machine import Pin
from time import sleep_ms, sleep


sta = network.WLAN(network.STA_IF) 
sta.active(True)
# sta.disconnect()      # For ESP8266

esp = espnow.ESPNow()
esp.active(True)
