RIPARIA
April 21, 2020/
May 12, 2020

This repository represents a live system. Its currently in use
controlling aspects of/collecting data on my 75 gallon Riparian tank.
It houses a number of live fish and plants. 

I'm treating it as a platform to learn about and experiment with 
Micropython. 

The system includes a Raspberry Pi running a MQTT broker 
(Mosquitto) and Node-Red. The esp boards (esp8266 and esp32)
are satellites running Micropython and using the umqtt module
to communicate with the Pi. 

Future Plans: 
- Adding stepper motor actuated valves to the plumbing
- Adding a camera and playing with image recognition/tracking
- Adding a Normally Closed solenoid valve to cut flow in case
  of a power out.
- flow-rate sensor
- ph sensor
- switching lights to PWM dimmers and animating transitions 
  (testing with lights.py BETA)
- Adding a WS2812b strips to the canopy for mood light and
  programming effects/ subtle star twinkles




