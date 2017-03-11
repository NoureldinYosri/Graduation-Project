import cv2
import numpy as np
from matplotlib import pyplot as plt
 
 
def get_mask(I):
	"""takes a 2d msk array of 0s and 1s"""
	if len(I) == 0 or len(I[0]) == 0: return 0;
	n = len(I);
	m = len(I[0]);
	for row in I:
		if len(row) != m:
			print "uneven dimensions ... aborting";
			return;
	row_sum = [0 for i in xrange(n)];
	col_sum = [0 for i in xrange(m)];
	row_sum2 = [0 for i in xrange(n)];
	col_sum2 = [0 for i in xrange(m)];
	msk = [[0 for j in xrange(m)] for i in xrange(n)];
	for i in xrange(n):
		for j in xrange(m):
			col_sum[j] += I[i][j];
			row_sum[i] += I[i][j];
	Th = 0;
	for i in xrange(n):
		for j in xrange(m):
			if I[i][j]: 
				msk[i][j] = I[i][j];
				row_sum2[i] += I[i][j];
				col_sum2[j] += I[i][j];
			else:
				msk[i][j] = (col_sum2[j] > Th) \
							 and (col_sum[j] - col_sum2[j] > Th) \
							and (row_sum2[i] > Th) \
							and (row_sum[i] - row_sum2[i] > Th);
				msk[i][j] = int(msk[i][j])*255;
			#	msk[i][j] = 0;
	return msk;
 
img = cv2.imread('1.jpg')
 
#get rid of very bright and very dark regions
delta=10
lower_gray = np.array([delta, delta,delta])
upper_gray = np.array([255-delta,255-delta,255-delta])
# Threshold the image to get only selected
mask = cv2.inRange(img, lower_gray, upper_gray)
# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)
#Convert to HSV space
HSV_img = cv2.cvtColor(res, cv2.COLOR_BGR2HSV)
hue = HSV_img[:, :, 0]
 
#select maximum value of H component from histogram
hist = cv2.calcHist([hue],[0],None,[256],[0,256])
hist= hist[1:, :] #suppress black value
elem = np.argmax(hist)
print np.max(hist), np.argmax(hist)
 
tolerance=20
lower_gray = np.array([elem-tolerance, 0,0])
upper_gray = np.array([elem+tolerance,255,255])
# Threshold the image to get only selected
mask = cv2.inRange(HSV_img, lower_gray, upper_gray)
#edit the mask to get the players

final_mask= get_mask(mask)
#print (len(mask))
#print (len(mask[0]))
final_mask=np.array(final_mask)
final_mask = np.array(final_mask * 255, dtype = np.uint8) 
#final_mask = mask;

#print (len(final_mask))
#print (len(final_mask[0]))
 
 
# Bitwise-AND mask and original image
res2 = cv2.bitwise_and(img,img, mask= final_mask)
 
cv2.imwrite("result.jpg", res2)
 
 
titles = ['Original Image', 'Selected Gray Values', 'Hue', 'Result']
images = [img, res, hue, res2]
for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
