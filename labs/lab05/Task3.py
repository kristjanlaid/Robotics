import numpy as np
import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow("Original")
trackbar_value_lR = 0
trackbar_value_lG = 0
trackbar_value_lB = 0
trackbar_value_hR = 125
trackbar_value_hG = 125
trackbar_value_hB = 125
def updateValue_lR(new_value_lR):
    global trackbar_value_lR
    trackbar_value_lR = new_value_lR
def updateValue_lG(new_value_lG):
    global trackbar_value_lG
    trackbar_value_lG = new_value_lG
def updateValue_lB(new_value_lB):
    global trackbar_value_lB
    trackbar_value_lB = new_value_lB
def updateValue_hR(new_value_hR):
    global trackbar_value_hR
    trackbar_value_hR = new_value_hR
def updateValue_hG(new_value_hG):
    global trackbar_value_hG
    trackbar_value_hG = new_value_hG
def updateValue_hB(new_value_hB):
    global trackbar_value_hB
    trackbar_value_hB = new_value_hB
    
cv2.createTrackbar("lR", "Original", trackbar_value_lR, 255, updateValue_lR)
cv2.createTrackbar("lG", "Original", trackbar_value_lG, 255, updateValue_lG)
cv2.createTrackbar("lB", "Original", trackbar_value_lB, 255, updateValue_lB)
cv2.createTrackbar("hR", "Original", trackbar_value_hR, 255, updateValue_hR)
cv2.createTrackbar("hG", "Original", trackbar_value_hG, 255, updateValue_hG)
cv2.createTrackbar("hB", "Original", trackbar_value_hB, 255, updateValue_hB)


blobparams = cv2.SimpleBlobDetector_Params()
blobparams.filterByArea = True
blobparams.minArea = 200
blobparams.maxArea = 10000
blobparams.filterByCircularity = False
blobparams.filterByInertia = False
blobparams.filterByConvexity = False
blobparams.minDistBetweenBlobs = 50
detector = cv2.SimpleBlobDetector_create(blobparams)


while True:
    ret, frame = cap.read()
    
    
    # You will need this later
    # frame = cv2.cvtColor(frame, ENTER_CORRECT_CONSTANT_HERE)
#     frame = cv2.cvtColor(frame, )
    # Colour detection limits
    
    lowerLimits = np.array([trackbar_value_lB, trackbar_value_lG, trackbar_value_lR])
    upperLimits = np.array([trackbar_value_hB, trackbar_value_hG, trackbar_value_hR])
    print(lowerLimits)
    print(upperLimits)
    thresholded = cv2.inRange(frame, lowerLimits, upperLimits)
    thresholded = cv2.bitwise_not(thresholded)
    outimage = cv2.bitwise_and(frame, frame, mask = thresholded)
    
    keypoints = detector.detect(thresholded)
    image = cv2.drawKeypoints(frame, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    for keypoint in keypoints:
        x = int(keypoint.pt[0])
        y = int(keypoint.pt[1])
        cv2.putText(image, (str("x: ") + str(x)), (x + 50, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        cv2.putText(image, (str("y: ") + str(y)), (x + 50, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow('Original', frame)
    cv2.imshow("image", image)
    cv2.imshow('Processed', thresholded)
    
    # Quit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print('closing program')
cap.release()
cv2.destroyAllWindows()


