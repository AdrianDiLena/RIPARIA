import esp32
import utime
import dht
import onewire
import ds18x20


led = machine.Pin(2, machine.Pin.OUT) # built-in LED for testing

# DS18x20 Temperature Sensors

pin = machine.Pin(5, machine.Pin.IN)
wire = onewire.OneWire(pin)
ds = ds18x20.DS18X20(wire)

# DHT22 Temperature Sensor

d = dht.DHT22(machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP))

# 8 Channel Relay Assignments

relay1 = machine.Pin(22, machine.Pin.OUT) # Lights: blue
relay2 = machine.Pin(32, machine.Pin.OUT) # Lights: red
relay3 = machine.Pin(33, machine.Pin.OUT) # Lights: white 
relay4 = machine.Pin(25, machine.Pin.OUT) # Lights: sump
relay5 = machine.Pin(26, machine.Pin.OUT) # Lights: night 
relay6 = machine.Pin(27, machine.Pin.OUT) # Air Pump 
relay7 = machine.Pin(14, machine.Pin.OUT) # Co2 Solenoid
relay8 = machine.Pin(13, machine.Pin.OUT) # Circulation Pump 



# LIGHTS
# Scheduled via Node-Red MQTT Topic 'RIPARIA_lights'

def sub_cb(topic, msg):
    print((topic, msg))
    if topic == b'RIPARIA_lights' and msg == b'blue_on':
        relay1.on()
    elif topic == b'RIPARIA_lights' and msg == b'blue_off':
        relay1.off()
    if topic == b'RIPARIA_lights' and msg == b'red_on':
        relay2.on()
    elif topic == b'RIPARIA_lights' and msg == b'red_off':
        relay2.off()
    if topic == b'RIPARIA_lights' and msg == b'white_on':
        relay3.on()
    elif topic == b'RIPARIA_lights' and msg == b'white_off':
        relay3.off()
    if topic == b'RIPARIA_lights' and msg == b'sump_on':
        relay4.on()
    elif topic == b'RIPARIA_lights' and msg == b'sump_off':
        relay4.off()
    if topic == b'RIPARIA_lights' and msg == b'night_on':
        relay5.on()
    elif topic == b'RIPARIA_lights' and msg == b'night_off':
        relay5.off()

    # OTHER SCHEDULED THINGS:

    if topic == b'RIPARIA_lights' and msg == b'air_on':
        relay6.on()
    elif topic == b'RIPARIA_lights' and msg == b'air_off':
        relay6.off()
    if topic == b'RIPARIA_lights' and msg == b'co2_on':
        relay7.on()
    elif topic == b'RIPARIA_lights' and msg == b'co2_off':
        relay7.off()
    if topic == b'RIPARIA_lights' and msg == b'circ_on':
        relay8.on()
    elif topic == b'RIPARIA_lights' and msg == b'circ_off':
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
    addr = ds.scan().pop()
    ds.convert_temp()
    time.sleep_ms(1000) # 750ms delay is required for the ds18x20 probe. Compensated for elsewhere. 
    temp = ds.read_temp(addr)
    d.measure()
    client.publish('RIPARIA_air_temp', str(d.temperature())) # publishes temp to mqtt broker
    client.publish('RIPARIA_humidity', str(d.humidity())) # publishes temp to mqtt broker
    client.publish('RIPARIA_temp_tank', str(temp))
    client.publish('RIPARIA_box_temp', str(esp32.raw_temperature()))
   # client.publish('RIPARIA_temp_sump', str(temp))
   # client.publish('RIPARIA_flow_meter', str(d.humidity()))
   # utime.sleep_ms(2000)



    try:
        client.check_msg()
    except OSError as e:
        restart_and_reconnect()
