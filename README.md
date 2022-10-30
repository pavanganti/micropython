# micropython
This repository contains code for running micropython projects.

temp_sensor.py
I am using DS18B20 temperature sensor to read the temperature. Based on the range of temp, the number of leds will be blinking and also the color will change.
Example:
if the temp is greater than 30 deg celcius:
   light upto 4 leds in red.
else if temp is in between 30 and 28 (inclusive):
   light upto 3 leds in yellow.
else if temp is in between 28 and 24 (inclusive):
   light upto 2 leds in blue
else:
   not enough temp to light the led bulbs
   
   
Ref: 
1. https://how2electronics.com/interfacing-ds18b20-sensor-with-raspberry-pi-pico/
2. http://www.coderdojotc.org/micropython/
