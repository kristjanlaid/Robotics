#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# reference pins by GPIO numbers
GPIO.setmode(GPIO.BCM)
# disable warnings
GPIO.setwarnings(False)

# define row and column pin numbers
row_pins = [21, 20, 16, 19, 13, 6, 5]
col_pins = [2, 3, 4, 14, 15]

# set all the pins as outputs and set column pins high, row pins low
GPIO.setup(col_pins, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(row_pins, GPIO.OUT, initial=GPIO.HIGH)

def show_row(row_number, columns, delay):
    # Control a row of the dot matrix display
    for i in columns:
        GPIO.output(col_pins[i-1], GPIO.HIGH)
    GPIO.output(row_pins[row_number - 1], GPIO.LOW)
    time.sleep(delay)
    for i in columns:
        GPIO.output(col_pins[i-1], GPIO.LOW)

    GPIO.output(row_pins[row_number - 1], GPIO.HIGH)

while True:
    show_row(6, [2, 3, 5], 0.01)
GPIO.cleanup()


