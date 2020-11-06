#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import signal
import time
import easygopigo3 as go
import read_sensors as sensors
import sys


def follow(robot, ls1, ls2, ls3, ls4, ls5):
    """
    TASK: Code for following the line based on line sensor readings
    """

    return


def markers_detected(ls1, on_marker, markers_count):
    """
    TASK: Code for detecting markers, update markers_count if needed
    """

    return markers_count


def close(message=""):
    """
    line_following specific cleanup function
    """
    global running, ser, robot
    print(message)
    running = False
    robot.stop()
    if ser.is_open:
        ser.close()
    sys.exit(0)


def signal_handler(sig, frame):
    """
    This function will be called when CTRL+C is pressed
    """
    close('\nYou pressed Ctrl+C! Closing the program nicely :)')


if __name__ == "__main__":
    # Register a callback for CTRL+C
    signal.signal(signal.SIGINT, signal_handler)

    robot = go.EasyGoPiGo3()
    robot.set_speed(60)

    running, ser = sensors.initialize_serial('/dev/ttyUSB0')

    markers_count = -100 # Change to correct value
    on_marker = False
    while running:
        arduino_data = sensors.get_data_from_arduino(ser)
        if arduino_data:
            ls1 = arduino_data['ls1']
            ls2 = arduino_data['ls2']
            ls3 = arduino_data['ls3']
            ls4 = arduino_data['ls4']
            ls5 = arduino_data['ls5']

            print("LS1: ", ls1, "LS2: ", ls2, "LS3: ", ls3, "LS4: ", ls4, "LS5: ", ls5)

            markers_count = (ls1, on_marker, markers_count)
            follow(robot, ls1, ls2, ls3, ls4, ls5)

        if not ser.is_open:
            close("Serial is closed!")

        # Throttle the loop to 50 times per second
        time.sleep(.02)
    close()
