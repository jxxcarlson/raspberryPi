#!/usr/bin/env python

# Test GPIO pins by blinking attadched LEDs

import sys
import argparse
import time
import RPi.GPIO as GPIO

HIGH = 1
LOW = 0

W2G = { 0:17, 1:18, 2:21, 3:22, 4:23, 5:24, 6:25, 7:4 }
B2G = { 7:4, 11:17, 12:18, 13:21, 15:22, 16:23, 18:24, 22:25 }

def printDictionary():

  print("")
  print("  Mapping from Wiring Pi to GPIO\n")
  for key in W2G.keys():
    print("    %2d ==> %2d" % (key, W2G[key]))
  print("")
  print("  Mapping from RPi Board to GPIO\n")
  for key in B2G.keys():
    print("    %2d ==> %2d" % (key, B2G[key]))
  print("")


def blink(LED, on, off):
  '''Test to see if outputPin is working.'''
  while True:
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(on)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(off)


def run():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(PIN, GPIO.OUT)
  blink( PIN, 0.1, 0.3  )


parser = argparse.ArgumentParser(description='Test GPIO pins by blinking them')

parser.add_argument('-b', action="store", dest="b", type=int, help='RPi board pin mode')
parser.add_argument('-g', action="store", dest="g", type=int, help='GPIO pin mode')
parser.add_argument('-w', action="store", dest="w", type=int, help='Wiring Pi pin mode')
parser.add_argument('-p', action="store_true", dest="p", help='Print pin map')

args = parser.parse_args()

print(args)

if args.b:
  PIN = B2G[args.b]
  print("RPi: %d" % args.b)
  run()

if args.g:
  PIN = args.g
  print("GPIO: %d" %args.g)
  run()

if args.w > -1:
  print("Wiring Pi: %d" % args.w)
  PIN = W2G[args.w]
  run()

if args.p:
  printDictionary()

