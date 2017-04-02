import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture('goal.mp4')
ballUpper = (200, 224, 220)
ballLower = (172, 184, 171)
#print(cap.get(cv2.cv.CV_CAP_PROP_FPS))


while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.waitKey(1)
    frame = imutils.resize(frame, width=480)
    frameCopy = frame.copy()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frame, ballLower, ballUpper)
    #gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_image_blurred = cv2.GaussianBlur(mask,(5,5),0)
    hough = cv2.HoughCircles(gray_image_blurred,cv2.cv.CV_HOUGH_GRADIENT,50,500,maxRadius=80)
    
    if hough is not None:
        hough = np.round(hough[0, :]).astype("int")
        for (x, y, r) in hough:
            cv2.circle(frameCopy, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(frameCopy, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            
    #cv2.imshow('frame',frameCopy)
    #cv2.imshow('mask',mask)
    cv2.waitKey(10)
    #cv2.imshow('gray',hough)
    cv2.imshow("output",np.hstack([frame,frameCopy]))
    cv2.waitKey(10)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()