import cv2
import numpy as np 

#green 245 : 255 , red 225 : 235
def getColor(img , x , y , rge ,minred,maxred,mingrn,maxgrn):
	image=img[x-rge:x+rge,y-rge:y+rge]
	red=image[:,:,2]
	green=image[:,:,1]
	ct=0
	for i in range (len(green)):
		for j in range (len(green[0])):
			if(red[i][j] > minred and red[i][j]< maxred and green[i][j] > minred and green[i][j] < maxgrn):
				ct+=1
	print ct
	return ct


img =cv2.imread('bar.jpg')
green=img[:,:,1]
blue=img[:,:,0]
red=img[:,:,2]
r=len(green)
c=len(green[0])
for i in range(r):
	for j in range(c):
		if(green[i][j]>red[i][j] and red[i][j]>blue[i][j]):
			continue
		else:
			img[i][j]=0
roi = img
gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) # convert color to gray
# gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
edges_frame = cv2.Canny(gray,255,250,apertureSize = 3) # edge detection
kernel = np.ones((3,3),np.uint8) # cretae mask 3*3 of ones
# dilation = cv2.dilate(edges_frame,kernel,iterations = 2)
# cv2.imshow('Contours', dilation)
# cv2.waitKey(0)

# cv2.imshow('dilation',dilation)
# cv2.waitKey(0)
# thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 1)
closing = cv2.morphologyEx(edges_frame, cv2.MORPH_CLOSE,kernel, iterations=1)
cont_img = closing.copy()
contours, hierarchy = cv2.findContours(cont_img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# print (contours)
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 2 or area > 100:
        continue
    if len(cnt) < 5:
        continue
    M = cv2.moments(cnt)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    dcolor=getColor(roi,cX,cY,30,200,250,200,250)
    if(dcolor>25 and dcolor < 35):
    	cv2.circle(roi, (cX, cY), 7, (0, 0, 255), -1)
    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(roi, ellipse, (0,255,0), 2)
cv2.imshow('Contours', roi)
cv2.imshow('field',img)
cv2.waitKey(0)
