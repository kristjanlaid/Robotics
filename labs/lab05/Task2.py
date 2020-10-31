#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import time

# Open the camera
cap = cv2.VideoCapture(0)
old_time = 0
new_time = 0



while True:
    # Read the image from the camera
    ret, frame = cap.read()
    
    new_time = time.time()
    Fps = 1 / (new_time - old_time)
    old_time = new_time
    Fps = int(Fps)
    Fps = str(Fps)

    # Write some text onto the frame
    cv2.putText(frame, Fps, (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show this image on a window named "Original"
    cv2.imshow('Original', frame)

    # Quit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
print('closing program')
cap.release()
cv2.destroyAllWindows()


