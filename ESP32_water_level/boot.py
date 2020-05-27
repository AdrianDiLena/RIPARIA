import time
from umqtt.simple import MQTTClient
import machine
import micropython
import network
import esp
import webrepl

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

print('\nRIPARIA - Water Marks:\nMeasure water levels and\nrefill aquarium sump with Mqtt\n')

print(station.ifconfig())
webrepl.start()
print('...............................')

