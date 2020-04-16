import esp32
import utime

led = machine.Pin(2, machine.Pin.OUT) # built-in LED for testing

relay1 = machine.Pin(00, machine.Pin.OUT) # Lights: red
relay2 = machine.Pin(00, machine.Pin.OUT) # Lights: blue
relay3 = machine.Pin(00, machine.Pin.OUT) # Lights: white 
relay4 = machine.Pin(00, machine.Pin.OUT) # Lights: sump 
relay5 = machine.Pin(00, machine.Pin.OUT) # relay : List Purpose. 
relay6 = machine.Pin(00, machine.Pin.OUT) # relay : List Purpose. 
relay7 = machine.Pin(00, machine.Pin.OUT) # relay : List Purpose. 
relay8 = machine.Pin(00, machine.Pin.OUT) # relay : List Purpose. 

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'testled' and msg == b'on':
    led.on()
  elif topic == b'testled' and msg == b'off':
    led.off()

def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  client.publish('testtemp', str(esp32.raw_temperature())) # publishes temp to mqtt broker
  utime.sleep_ms(2000)




  try:
    client.check_msg()
  except OSError as e:
    restart_and_reconnect()
