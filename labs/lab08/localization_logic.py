#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import easygopigo3 as go
import time
import signal
import cv2
import threading
import line_following as line
import numpy as np
import read_sensors as sensors
from visualisation import RepeatTimer
import sys

on_marker1 = False
# Dictionary for holding positions
positions = {'current_marker': 0, 'current_us': -1, 'current_enc': -1, 'current_cam': -1}


def fast_worker(running, robot, positions, ser, close_function):
    """
    Fastworker logic
    A while-loop with the main control logic and should be used for fast processes.
    """

    print("Starting fastWorker in a separate thread")

    # Distance from the START marker to the wall in mm
    start_to_wall_dist = 1600
    markers_count = 0
    robot.reset_encoders(blocking=True)
    last_ls1 = 1
    while running:
        arduino_data = sensors.get_data_from_arduino(ser)
        
        
        """
        TASK: Get the averaged encoder value and use it to
        find the distance from the wall in millimetres
        positions['current_enc'] = ...
        """
        positions['current_enc'] = start_to_wall_dist - (round(robot.read_encoders_average(units='cm')) * 10)
        positions['current_enc_improved'] = positions['current_enc']
        if arduino_data:
            ls1 = arduino_data['ls1']
            ls2 = arduino_data['ls2']
            ls3 = arduino_data['ls3']
            ls4 = arduino_data['ls4']
            ls5 = arduino_data['ls5']
            us_pos = arduino_data['us']

            """
            TASK: save current ultrasonic position to positions dictionary
            """
            positions['current_us'] = us_pos
            positions['current_marker'] = line.markers_detected(ls1, last_ls1, positions['current_marker'])
            line.follow(robot, ls1, ls2, ls3, ls4, ls5)
            print(markers_count)
            if positions['current_marker'] == 7:
                robot.stop()
            """
            Add the rest of your line following & marker detection logic
            """
            
        if not ser.is_open:
            close_function("Serial is closed!")

        # Limit control thread to 50 Hz
        time.sleep(0.02)

    close_function("Fast_worker closed!")


def detect_blobs(frame):
    """
    Image processing and blob detection logic
    """
    keypoints = []

    return keypoints


def get_blob_size(keypoints):
    """
    Find the size of biggest keypoint
    """
    max_size = 0

    return max_size


def get_distance_with_cam(blob_size):
    """
    Calculate distance based on blob size
    """
    return -1


def slow_worker():
    """
    Slower code
    Low update rate is suitable for slow processes, such as image processing, displaying data to graph, etc;
    """
    global positions

    ret, frame = cap.read()

    # Get the blob size and convert it to distance from the wall
    keypoints = detect_blobs(frame)
    blob_size = get_blob_size(keypoints)
    positions['current_cam'] = get_distance_with_cam(blob_size)

    print(positions)
    image_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (0, 0, 255),
                                             cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Camera image", image_with_keypoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        close("Image closed")


# This function will be called when CTRL+C is pressed
def signal_handler(sig, frame):
    """
    This function will be called when CTRL+C is pressed, read_sensors specific
    """
    close('\nYou pressed Ctrl+C! Closing the program nicely :)')


def close(message=""):
    """
    localization_logic specific cleanup
    """
    global running, ser, robot, timer
    print(message)
    running = False
    robot.stop()
    if ser.is_open:
        ser.close()
    timer.cancel()
    if fast_thread.is_alive:
        try:
            fast_thread.join()
        except:
            pass
    sys.exit(0)


if __name__ == "__main__":
    # Register a callback for CTRL+C
    signal.signal(signal.SIGINT, signal_handler)

    running, ser = sensors.initialize_serial('/dev/ttyUSB0')

    robot = go.EasyGoPiGo3()
    robot.set_speed(60)

    # Open the camera
    cap = cv2.VideoCapture(0)

    # Create fast_worker in a separate thread.
    fast_thread = threading.Thread(
        target=fast_worker,
        args=(running, robot, positions, ser, close)
    )
    fast_thread.daemon = True
    fast_thread.start()

    timer = RepeatTimer(0.1, slow_worker)
    timer.start()

    while running:
        time.sleep(1)
    close()
