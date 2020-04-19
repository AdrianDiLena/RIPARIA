import esp32
import utime

led = machine.Pin(2, machine.Pin.OUT) # built-in LED for testing

# DS18x20 Temperature Sensors

pin = machine.Pin(12)
wire = onewire.OneWire(pin)
ds = ds18x20.DS18X20(wire)

# DHT22 Temperature Sensor

d = dht.DHT22(machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP))

# 8 Channel Relay

relay1 = machine.Pin(00, machine.Pin.OUT) # Lights: red
relay2 = machine.Pin(00, machine.Pin.OUT) # Lights: blue
relay3 = machine.Pin(00, machine.Pin.OUT) # Lights: white 
relay4 = machine.Pin(00, machine.Pin.OUT) # Lights: sump 
relay5 = machine.Pin(00, machine.Pin.OUT) # Lights: night 
relay6 = machine.Pin(00, machine.Pin.OUT) # Air Pump 
relay7 = machine.Pin(00, machine.Pin.OUT) # Co2 Solenoid
relay8 = machine.Pin(00, machine.Pin.OUT) # Circulation Pump 

addr = ds.scan().pop()
ds.convert_temp()
time.sleep_ms(750)
temp = ds.read_temp(addr)

# LIGHTS
# Scheduled via Node-Red MQTT Topic 'RIPARIA'

def sub_cb(topic, msg):
    print((topic, msg))
    if topic == b'RIPARIA' and msg == b'red_on':
        relay1.on()
    elif topic == b'RIPARIA' and msg == b'red_off':
        relay1.off()
    if topic == b'RIPARIA' and msg == b'blue_on':
        relay2.on()
    elif topic == b'RIPARIA' and msg == b'blue_off':
        relay2.off()
    if topic == b'RIPARIA' and msg == b'white_on':
        relay3.on()
    elif topic == b'RIPARIA' and msg == b'white_off':
        relay3.off()
    if topic == b'RIPARIA' and msg == b'night_on':
        relay4.on()
    elif topic == b'RIPARIA' and msg == b'night_off':
        relay4.off()
    if topic == b'RIPARIA' and msg == b'sump_on':
        relay5.on()
    elif topic == b'RIPARIA' and msg == b'sump_off':
        relay5.off()

    # OTHER SCHEDULED THINGS:

    if topic == b'RIPARIA' and msg == b'air_on':
        relay6.on()
    elif topic == b'RIPARIA' and msg == b'air_off':
        relay6.off()
    if topic == b'RIPARIA' and msg == b'co2_on':
        relay7.on()
    elif topic == b'RIPARIA' and msg == b'co2_off':
        relay7.off()
    if topic == b'RIPARIA' and msg == b'circ_on':
        relay8.on()
    elif topic == b'RIPARIA' and msg == b'circ_off':
        relay8.off()

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
    client.publish('testtemp', str(esp32.hall_sensor())) # publishes temp to mqtt broker
    utime.sleep_ms(2000)



    try:
        client.check_msg()
    except OSError as e:
        restart_and_reconnect()
