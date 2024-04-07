# Use this snippet on your receiver board to find the MAC address.
import network

wlan = network.WLAN(network.STA_IF)
mac_address = wlan.config('mac')

print(mac_address)

# The result will be like: b'`\x01\x94I\xf2\x90'
# Exactly use it within transmiter snippet without any change in foramt
