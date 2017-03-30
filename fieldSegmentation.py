import cv2
import numpy as np
img = cv2.imread('a1.jpg')          # Video Frame 
green = img[:,:,1]                  # Green Component in Pixel
blue = img[:,:,0]					# Blue Component in Pixel
red = img[:,:,2]					# Red Component in Pixel
r = len(green)
c = len(green[0])
for i in range(r):
    for j in range(c):
        if(green[i][j]>red[i][j] and red[i][j]>blue[i][j]):
            continue
        else:
            img[i][j]=0
cv2.imshow('img', img)
cv2.waitKey(0)