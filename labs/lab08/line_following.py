#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import signal
import time
import easygopigo3 as go
import read_sensors as sensors
import sys

on_marker1 = False
def follow(robot, ls1, ls2, ls3, ls4, ls5):
    """
    TASK: Code for following the line based on line sensor readings
    """
    if ls3 == 0:
        robot.forward()
    elif ls5 == 0 or ls4 == 0:
        robot.right()
    elif ls1 == 0 or ls2 == 0:
        robot.left()
    return


def markers_detected(ls1, on_marker, markers_count):
    """
    TASK: Code for detecting markers, update markers_count if needed
    """
    global on_marker1
    if on_marker1 == False and ls1 == 0:
        on_marker1 = True
        markers_count += 1
    elif on_marker1 == True and ls1 == 1:
        on_marker1 = False
    if markers_count == 1:
        print('Distance from wall', 180, 'cm')
    elif markers_count == 2:
        print('Distance from wall', 160, 'cm')
    elif markers_count == 3:
        print('Distance from wall', 138, 'cm')
    elif markers_count == 4:
        print('Distance from wall', 110, 'cm')
    elif markers_count == 5:
        print('Distance from wall', 70, 'cm')
    elif markers_count == 6:
        print('Distance from wall', 40, 'cm')
    else:
        print('Distance from wall', 20, 'cm')
    
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

    markers_count = 0 # Change to correct value
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

            markers_count = markers_detected(ls1, on_marker, markers_count)
            follow(robot, ls1, ls2, ls3, ls4, ls5)
            print(markers_count)
            if markers_count == 7:
                robot.stop()
        if not ser.is_open:
            close("Serial is closed!")

        # Throttle the loop to 50 times per second
        time.sleep(.02)
    close()
