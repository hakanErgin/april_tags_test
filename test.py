import cv2
import numpy as np
from apriltag import apriltag

imagepath = 'bots.jpg'
image = cv2.imread(imagepath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

detector = apriltag("tag36h11")

detections = detector.detect(gray)

for detection in detections:
    lb, rb, rt, lt = detection["lb-rb-rt-lt"]
    # numpy.float64 to int
    lb_ = (int(lb[0]), int(lb[1]))
    rb_ = (int(rb[0]), int(rb[1]))
    rt_ = (int(rt[0]), int(rt[1]))
    lt_ = (int(lt[0]), int(lt[1]))
    
    cv2.line(image, lb_, rb_, (0, 255, 0), 2)
    cv2.line(image, rt_, rb_, (0, 255, 0), 2)
    cv2.line(image, rt_, lt_, (0, 255, 0), 2)
    cv2.line(image, lt_, lb_, (0, 255, 0), 2)

cv2.imshow('', image)
cv2.waitKey()
