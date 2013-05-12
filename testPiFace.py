#!/usr/bin/env python

'''
A few functons to get started with the PiFace IO Board.

Notes on the Python code: (i) use on(7) and
off(7) to turn the LED on an off manually; 7 is the pin
the LED is wired to; (ii) use code&gt;blink(7) for a more
exciting test; (iii) use code&gt;read(0) to read the switch,
which is attached to pin 0; (iv) use code&gt;control(7,0) to
control LED on pin 7 by the switch on pin 0.  Of course all this is
ridiculous overkill, but the idea is to get started.

'''

# Run this before runnng python: sudo modprobe spi-bcm2708 

import piface.pfio as pfio
from time import sleep


pfio.init()


HIGH = 1
LOW = 0
delay = 0.2 ## seconds

def on(LED):
  pfio.digital_write(LED, HIGH)

def off(LED):
  pfio.digital_write(LED, LOW)

def blink(LED):
  while True:
    pfio.digital_write(LED, HIGH)  
    sleep(delay)
    pfio.digital_write(LED, LOW)
    sleep(delay)

def read(n):
  '''Read switch n. If it is closed, print "ON".'''
  while True:
    if pfio.digital_read(n):
      print("ON")

def control(LED, switch):
  while True:
    if pfio.digital_read(switch):
      pfio.digital_write(LED, HIGH)
    else:
      pfio.digital_write(LED, LOW)

if __name__ == '__main__':
   control(7,0)

