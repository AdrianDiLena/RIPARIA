RIPARIA
April 21, 2020

This repository represents a live system. Its currently in use
controlling aspects of/collecting data on my Riparian tank. 

The system includes a Raspberry Pi running a MQTT broker 
(Mosquitto) and Node-Red. The esp boards (esp8266 and esp32)
are satellites running Micropython and using the umqtt module
to communicate with the Pi. 

Future Plans: 
- Adding stepper motor actuated valves to the plumbing
- Adding a Normally Closed solenoid valve to cut flow in case
  of a power out.
- flow-rate sensor
- ph sensor
- Adding a WS2812b strips to the canopy for mood light and
  programming effects/ subtle star twinkles




