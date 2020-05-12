import time
from umqtt.simple import MQTTClient
import machine
import micropython
import network
import esp

import gc
gc.collect()

ssid = 'VIRGIN930'
password = '6AF7AD59'
client_id = '756345364758574'
mqtt_server = '192.168.2.67'
#topic_sub = b'RIPARIA_lights'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print(station.ifconfig())

print('\n')
print('Welcome to Riparia')
print('Networked Aquarium System')
print('Adrian DiLena')
print('22.04.2020')
print('Water Level Sensor and Refill // D1 Mini ESP8266')
print('\n')
print('"Another flaw in the human character\nis that everyone wants to build and no one\nwants to do maintenance"\n- Kurt Vonnegut')

