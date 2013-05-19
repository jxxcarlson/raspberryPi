#!/usr/bin/env python

import sys
import time
import RPi.GPIO as GPIO

HIGH = 1
LOW = 0

Q2W = { 0:17, 1:18, 2:21, 3:22, 4:23, 5:24, 6:25, 7:4 }

def setup(outputPin):
  '''Call setup() before doing anything else.'''
  GPIO.setmode(GPIO.BCM)
  # GPIO.setmode(GPIO.BOARD)


def blink(LED, on, off):
  '''Test to see if outputPin is working.'''
  while True:
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(on)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(off)


args = sys.argv

def message():
  print("")
  print("  blink OPTION PIN, where OPTION  = -g|-b|-w")
  print("  -g  == GPIO numbering, RPi board numberuing, -w = WIRING PI")
  print("")

mode = "-g"

if len(args) == 3:

  mode = args[1]
  PIN = int (args[2])

  if mode == "-g": 
    GPIO.setmode(GPIO.BCM)
  elif mode == "-b":
    GPIO.setmode(GPIO.BOARD)
  elif mode == "-w":
    GPIO.setmode(GPIO.BCM)
  else:
    message(); exit();

elif len(args) == 2:
  if args[1] == "-h":
    message(); exit();
  else:
    PIN = int (args[1])
    GPIO.setmode(GPIO.BCM)


if mode == "-w":
  PIN = Q2W[PIN]

if len(args) == 1:
  message(); exit()

GPIO.setup(PIN, GPIO.OUT)
blink( PIN, 0.1, 0.3  )
