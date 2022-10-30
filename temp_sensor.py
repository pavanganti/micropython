import machine, onewire, ds18x20, time
from machine import Pin
from neopixel import NeoPixel
from time import sleep

#Global variables
ds_pin = machine.Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()
temp=""
LED_PIN = 0
NUMBER_PIXELS = 60
strip = NeoPixel(Pin(LED_PIN), NUMBER_PIXELS)

def light_leds(num_leds: int):
    print('lighting leds')
    print('num leds: {} '.format(num_leds))
    switch_off_lights()
       
    if num_leds == 4:
        red_color = 255
        blue_color = 0
        green_color = 0
    elif num_leds == 3:
        red_color = 255
        blue_color = 0
        green_color = 255
    elif num_leds == 2:
        red_color = 0
        blue_color = 255
        green_color = 0     
    
    for i in range(0, num_leds):
        strip[i] = (red_color,green_color,blue_color) 
        strip.write() # send the data from RAM down the wire
        sleep(.1) # keep on 1/10 of a second
        strip[i] = (0,0,0) # change the RAM back but don't resend the data

def switch_off_lights():
    print('Switching off all leds local function...')
    for i in range (LED_PIN,NUMBER_PIXELS):
        strip[i] = (0,0,0)



print('Found DS devices: ', roms)
switch_off_lights()
print('after the function')

while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    #print(rom)
    temp = ds_sensor.read_temp(rom)
    print('temperature in centigrade is: ',temp)
    if temp >= 30:
        print('light 4 leds in red color')
        light_leds(4)
    elif temp < 30 and temp >= 28:
        print('light 3 leds in yellow color')
        light_leds(3)
    elif temp < 28 and temp >= 24:
        print('light 2 leds in blue color')
        light_leds(2)
    else:
        print('raw is too small to power up an LED')
        
  #time.sleep(2)
    
