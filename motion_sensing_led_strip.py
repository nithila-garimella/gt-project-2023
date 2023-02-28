import time
import board
from neopixel import NeoPixel
import RPi.GPIO as GPIO

led_count = 10
motion_sensor_input = 10
led_strip_pin = board.D18

RED = (10,0,0)
GREEN = (0,10,0)
NO_COLOR = (0,0,0)

print('Started')

led_strip = NeoPixel(led_strip_pin, led_count, auto_write=False)

def turn_off():
    for i in range(0,led_count):
       led_strip[i] = NO_COLOR
    led_strip.show()

def turn_on():
    turn_off()
    for i in range(0,led_count):
              led_strip[i] = GREEN
              time.sleep(0.1)
              led_strip.show()
    turn_off()
    for i in range(0,led_count-1):
              led_strip[led_count-1-i] = RED
              time.sleep(0.1)
              led_strip.show()
   
GPIO.setwarnings(False)
GPIO.setup(motion_sensor_input, GPIO.IN)

turn_off()

while True:
    if(GPIO.input(motion_sensor_input)):
        print('motion detected')
        turn_on()
    else:
        print('no motion detected')
        turn_off()
