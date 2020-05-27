from umqtt.robust import MQTTClient
from machine import Pin
import machine
import time
import utime


led = machine.Pin(2, machine.Pin.OUT) # Builtin LED for testing. 
trig = Pin(16,Pin.OUT, pull=None) 
echo = Pin(17, Pin.IN, pull=None) 
trig.value(0)
echo.value(0) 

#UMQTT setup
client = MQTTClient('124748937892378493273655', '192.168.2.67') #unique id, umqtt broker ip
client.connect()

def send_pulse_and_wait(echo_timeout_us=500*2*30):
        trig.value(0) # Stabilize the sensor
        time.sleep_us(5)
        trig.value(1) # Send a 10us pulse.
        time.sleep_us(10)
        trig.value(0)
        try:
            pulse_time = machine.time_pulse_us(echo, 1, echo_timeout_us)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110: # 110 = ETIMEDOUT
                raise OSError('Out of range')
            raise ex

def distance_cm():
        pulse_time = send_pulse_and_wait()
        cms = (pulse_time / 2) / 29.1
        return cms
 
def main():
  threshold_count = 0
  threshold = 8 # Number of consecutive readings needed to trigger pump pin. 
  distance_threshold = 14 # distance in cm / adjust as needed.
  
  try:
    while True:
      utime.sleep_ms(5000) # Time between readings.
      distance = distance_cm()
      print('Distance: ' + str("%.2f" % distance) + ' cm // Count: ' + str(threshold_count))
      if distance > distance_threshold:
        threshold_count += 1
      else:
        threshold_count = 0
      if threshold_count >= threshold: 
        print('\nCommencing Refill\n')
        client.publish('RIPARIA/relays/system/waterpump', 'on')  
        led.on()                 # If 8 readings over threshold 
        while True:   
          utime.sleep_ms(1000)     #MQTT msg to turn on pump
          client.publish('RIPARIA/system/reservoirLevel', str(distance)) # Publish distance reading in this while loop
          print('Distance: ' + str("%.2f" % distance_cm()) + ' // Count: ' + str(threshold_count) + ' - Refilling...')
          if distance_cm() > 12:                          
            continue
          else:
            client.publish('RIPARIA/relays/system/waterpump', 'off')
            led.off()
            print('\nRefill Complete \nYou are Welcome.\n')   # MQTT msg to turn off pump
            break

      client.publish('RIPARIA/system/reservoirLevel', str(distance)) 
        
  except KeyboardInterrupt:
            pass

main()