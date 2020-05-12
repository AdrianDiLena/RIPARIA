import time
from umqtt.simple import MQTTClient
import machine
import micropython
import network
import esp
import webrepl
import gc
gc.collect()

# Relevant Personal Keys
ssid = 'VIRGIN930'
password = '6AF7AD59'
client_id = '756345364758574'
mqtt_server = '192.168.2.67'
topic_sub = b'RIPARIA/relays/#'

# Set up wifi station
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print(station.ifconfig())
webrepl.start()

print('\nWelcome to Riparia')
print('\nAdrian DiLena')
print('First Run: 22.04.2020')
print('This Version: 5.05.2020')
print('\nMain Controller and Monitor on ESP32')

