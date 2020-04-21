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
topic_sub = b'RIPARIA_lights'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print(station.ifconfig())

print('\n')
print('Welcome to Riparia')
print('     Version: Beta 0.001\n          Threat Level: Midnight')
print('     Adrian DiLena')
print('18.04.2020\n \n- Water Level Sensor on D1 Mini)
print('\n')

