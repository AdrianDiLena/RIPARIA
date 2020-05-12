import esp32
import utime
import dht
import onewire
import ds18x20
import webrepl
import lights


led = machine.Pin(2, machine.Pin.OUT) # built-in LED for testing

# Setting up ONEWIRE for DS18x20 Temperature Sensors

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
# Scheduled via Node-Red MQTT Topic 'RIPARIA/lights/

def sub_cb(topic, int):
    print((topic, msg))
    if topic == b'RIPARIA/relays/lights/blue' and msg == b'on':
        relay1.off()      # This model of ESP32 board has on/off gpio reversed for some reason. 
    elif topic == b'RIPARIA/relays/lights/blue' and msg == b'off':
        relay1.on()
    if topic == b'RIPARIA/relays/lights/red' and msg == b'on':
        relay2.off()
    elif topic == b'RIPARIA/relays/lights/red' and msg == b'off':
        relay2.on()
    if topic == b'RIPARIA/relays/lights/white' and msg == b'on':
        relay3.off()
    elif topic == b'RIPARIA/relays/lights/white' and msg == b'off':
        relay3.on()
    if topic == b'RIPARIA/relays/lights/sump' and msg == b'on':
        relay4.off()
    elif topic == b'RIPARIA/relays/lights/sump' and msg == b'off':
        relay4.on()
    if topic == b'RIPARIA/relays/lights/night' and msg == b'on':
        relay5.off()
    elif topic == b'RIPARIA/relays/lights/night' and msg == b'off':
        relay5.on()

    # OTHER SCHEDULED THINGS:

    if topic == b'RIPARIA/relays/system/airpump' and msg == b'on':
        relay6.off()
    elif topic == b'RIPARIA/relays/system/airpump' and msg == b'off':
        relay6.on()
    if topic == b'RIPARIA/relays/system/co2' and msg == b'on':
        relay7.off()
    elif topic == b'RIPARIA/relays/system/co2' and msg == b'off':
        relay7.on()
    if topic == b'RIPARIA/relays/system/waterpump' and msg == b'on':
        relay8.off()
    elif topic == b'RIPARIA/relays/system/waterpump' and msg == b'off':
        relay8.on()

def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_server)
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(topic_sub)
    print('Connected to: %s \nSubscribed to: %s' % (mqtt_server, topic_sub))
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
    espTemp = (esp32.raw_temperature()-32)*5/9

    d.measure()
    client.publish('RIPARIA/system/airtemp', str("%.2f" % d.temperature())) # publishes temp to mqtt broker
    client.publish('RIPARIA/system/humidity', str("%.2f" % d.humidity())) # publishes temp to mqtt broker
    client.publish('RIPARIA/system/tanktemp', str("%.2f" % temp))
    client.publish('RIPARIA/system/esp32temp', str("%.2f" % espTemp))

    # Debugging & Terminal prints
    print('Air Temperature:     ' + str("%.2f" % d.temperature()) + 'C')
    print('Relative Humidity:   ' + str("%.2f" % d.humidity()) + '%')
    print('Water Temperature:   ' + str("%.2f" % temp) + 'C')
    print('ESP32 Board Temp:    ' + str("%.2f" % espTemp) + 'C')
    print('---------------------------------')

    try:
        client.check_msg()
    except OSError as e:
        restart_and_reconnect()
