# Please note this was taken from pyimagesearch.com
# thank you and have a good day

import datetime
import time
import cv2


def motionDetectedEvent():
    pass


def motionDetection():
    motionCounter = 0
    running = True
    lastUploaded = datetime.datetime.now()
    avg = None

    camera = cv2.VideoCapture(0)
    
    while running:
        
        _, img = camera.read()
        frame = img
        timestamp = datetime.datetime.now()

        # resize the frame, convert it to grayscale, and blur it
        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # if the average frame is None, initialize it
        if avg is None:
            avg = gray.copy().astype("float")
            rawCapture.truncate(0)
            continue

        # accumulate the weighted average between the current frame and
        # previous frames, then compute the difference between the current
        # frame and running average
        cv2.accumulateWeighted(gray, avg, 0.5)
        frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))

        # threshold the delta image, dilate the thresholded image to fill
        # in holes, then find contours on thresholded image
        thresh = cv2.threshold(frameDelta, 5, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motionDetected = False

        # loop over the contours
        for c in cnts:
            # if the contour is too small, ignore it
            if cv2.contourArea(c) < 5000:
                continue

            # compute the bounding box for the contour, draw it on the frame,
            # and update the text
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            motionDetected = True

        # check to see if the room is occupied
        if motionDetected:
            # check to see if enough time has passed between uploads
            if (timestamp - lastUploaded).seconds >= 3.0:
                # increment the motion counter
                motionCounter += 1

                # check to see if the number of frames with consistent motion is
                # high enough
                if motionCounter >= 8:
                    motionDetectedEvent()
                    lastUploaded = timestamp
                    motionCounter = 0

        # otherwise, the room is not occupied
        else:
            motionCounter = 0

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)