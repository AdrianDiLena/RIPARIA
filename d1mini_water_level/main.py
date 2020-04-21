from umqtt.robust import MQTTClient
from machine import Pin
import machine
import time
import utime

pump = machine.Pin(2, machine.Pin.OUT) # Builtin LED for testing. 
trig = Pin(4,Pin.OUT, pull=None) #D2 on D1 Mini
echo = Pin(5, Pin.IN, pull=None) #D1 on D1 Mini
trig.value(0)
echo.value(0)

pump.on() # for some reason on is off/off is on. This is just to ensure that the pin is indeed low. 

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
      utime.sleep_ms(1000) # Time between readings.
      distance = distance_cm()
      print(distance)
      if distance > distance_threshold:
        threshold_count += 1
      else:
        threshold_count = 0
      if threshold_count >= threshold:
        #client.publish('RIPARIA_lights', 'circ_off')
        utime.sleep(1)
        #client.publish('RIPARIA_lights', 'circ_on')
      client.publish('RIPARIA_wLevel', str(distance)+'cm') 
        
  except KeyboardInterrupt:
            pass

main()