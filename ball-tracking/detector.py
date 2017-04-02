import cv2
import numpy as np
from matplotlib import pyplot as plt

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 	print v
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged

def fun(I):
	n = len(I);
	m = len(I[0]);
	for i in range(2,n-2):
		for j in range(2,m-2):
				a=i-1
				b=i+1
				c=j-1
				d=j+1
				acc=0
				for o in range(a,b):
					for q in range(c,d):
						if I[o][q]:
							acc+=1
							# print (i,j)
				print (acc)
				if(acc>=2):
					# if I[i][j] and I[i-1][j] and I[i-1][j-1] and I[i][j-1] :
						print(i,j)

				
frame = cv2.imread('result8.jpg')

gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# edges_frame = cv2.Laplacian(gray_frame, cv2.CV_64F)
edges_frame = cv2.Canny(gray_frame,255,250,apertureSize = 3)
# edges_frame = auto_canny(gray_frame)
kernel = np.ones((11,11),np.uint8)
dilation = cv2.dilate(edges_frame,kernel,iterations = 1)
cv2.imwrite("d2.jpg", dilation)

erosion = cv2.erode(dilation,kernel,iterations = 1)
print (erosion)
# fun(erosion/255)
# Set up the detector with default parameters.
# detector = cv2.SimpleBlobDetector()
circles = cv2.HoughCircles(erosion, cv2.cv.CV_HOUGH_GRADIENT, 1, 10,
              param1=30,
              param2=10,
              minRadius=0,
              maxRadius=0)

print circles
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('circles', frame)
# # Detect blobs.
# keypoints = detector.detect(erosion)
 
# # Draw detected blobs as red circles.
# # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
# im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (255,155,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# # Show keypoints
# cv2.imshow("Keypoints", im_with_keypoints)
# opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel)
# cv2.imshow('closing',erosion)
# cv2.imwrite("keypints.jpg", im_with_keypoints)
# titles = ['Original Image', 'Selected Gray Values', 'dilation', 'erosion']
# images = [frame, edges_frame, dilation, erosion]
# for i in xrange(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

cv2.waitKey(0)

