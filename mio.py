'''
mio.py:

The very basics of GPIO, with one output, e.g, an LED on pin 17,
and one input, e.g., a switch on pin 23.  
  
  SYNOPSIS:

  blink(LED, 0.1, 0.3)  -- blinks LED.  It is on for 0.1 second, 
                           off for 0.3 seconds.

  simpleRead(SWITCH)    -- reads SWITCH and report if it is on.

  read(SWITCH)          -- more sophisticated read function.
                           It prints "ON" when it detects that
                           the switch is closed.  When it finds
                           that it is open, it print the time
                           in seconds that it has been closed,
                           the prints "OFF".

  control(LED, SWITCH)  -- When SWITCH is closed, the LED flashes.
                           When SWITCH is open, the LED is dark.
                           The same information is printed as
                           for the function read().

CIRCUIT:

Let the switch have terminals A and B.

   A --- 3.3V

              |--- 1K resistor --- Pin 23
   B --- T ---|
              |--- 10K resistor ---GND

   Pin 17 --- LED --- 330 Ohm resistor --- GND                  

'''


import time
import RPi.GPIO as GPIO

LED = 17      # output
SWITCH = 23   # input
HIGH = 1
LOW = 0

WAITING = 0
DOWN = 1
UP = 2

NAPTIME = 0.01  # time in seconds that hte  program stays in sleep mode.  
                # A value of 0.01 seconds works and lowers the cpu load 
                # from 95% to 1.  If NAPTIME is too long, the program 
                # will respond poorly to user input.


def setup(outputPin, inputPin):
  '''Call setup() before doing anything else.'''
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(outputPin, GPIO.OUT)
  GPIO.setup(inputPin, GPIO.IN)

def blink(outputPin, on, off):
  '''Test to see if outputPin is working.'''
  while True:
    GPIO.output(outputPin, GPIO.HIGH)
    time.sleep(on)
    GPIO.output(outputPin, GPIO.LOW)
    time.sleep(off)

def simpleRead(inputPin):
  '''Read state of input pin ane report on it.'''
  count = 0
  while True:
    if GPIO.input(inputPin):
      count += 1;
      print("%5d: inputPin pressed" % count)
      GPIO.output(outputPin, HIGH)
    else:
      GPIO.output(outputPin, LOW)
    time.sleep(NAPTIME)  # Sleep for a short while


def read(inputPin):
  '''Read PIN and report how long it was pressed.'''
  state = WAITING
  while True:
    if (state == WAITING) & GPIO.input(inputPin):
      state = DOWN
      start_time = time.time()
      print("ON")
    if (state == DOWN) & (not GPIO.input(inputPin)):
      state = UP
      elapsed_time = time.time() - start_time
      print("%1.2f" % elapsed_time)
      print("OFF\n")
    if state == UP:
      state = WAITING 
    time.sleep(NAPTIME)  # Sleep for a short while

def control(outputPin, inputPin):
  '''Read the inputPin and report how long it was pressed.
  Switch the outputPin betwen HIGH and LOW when the inputPin is HIGH.'''
  state = WAITING
  while True:
    if (state == WAITING) & GPIO.input(inputPin):
      state = DOWN
      start_time = time.time()
      GPIO.output(outputPin,1)
      print("ON")
    if (state == DOWN) & (not GPIO.input(inputPin)):
      state = UP
      elapsed_time = time.time() - start_time
      print("%1.2f" % elapsed_time)
      print("OFF\n")
    if (state == DOWN) & GPIO.input(inputPin):
      elapsed_time = time.time() - start_time
      if elapsed_time % 0.5 < 0.2:
        GPIO.output(outputPin,1)
      else:
        GPIO.output(outputPin,0)
    if state == UP:
      state = WAITING
      GPIO.output(outputPin,0)
    time.sleep(NAPTIME)  # Sleep for a short while

if __name__ == '__main__':
  setup(LED, SWITCH)
  control(LED, SWITCH)
