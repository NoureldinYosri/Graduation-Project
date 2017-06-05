import numpy as np
import cv2
import pybgs

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
	for i in xrange(n):
		for j in xrange(m):
			if I[i][j]: 
				msk[i][j] = 1;
				row_sum2[i] += 1;
				col_sum2[j] += 1;
			else:
				msk[i][j] = (col_sum2[j] > 10) \
							 and (col_sum[j] - col_sum2[j] > 10) \
							and (row_sum2[i] > 10) \
							and (row_sum[i] - row_sum2[i] > 10);
				msk[i][j] = int(msk[i][j]);
	return msk;
def getColor(img , x , y , rge ,minred,maxred,mingrn,maxgrn):
	image=img[x-rge:x+rge,y-rge:y+rge]
	red=image[:,:,2]
	green=image[:,:,1]
	ct=0
	for i in range (len(green)):
		for j in range (len(green[0])):
			if(red[i][j] > minred and red[i][j]< maxred and green[i][j] > minred and green[i][j] < maxgrn):
				ct+=1
	# print ct
	return ct

#get rid of very bright and very dark regions


# params = { 
# 	'algorithm': 'eigenbackground', 
# 	'low': 15 * 15,
# 	'high': 15 * 15 * 2,
# 	'history_size': 100,
# 	'dims': 5 }

# params = { 
#  	'algorithm': 'adaptive_median', 
#  	'low': 40,
#  	'high': 40 * 2,
#  	'sampling_rate': 10,
#  	'learning_frames': 400 }

# params = { 
# 	'algorithm': 'grimson_gmm', 
# 	'low': 3.0 * 3.0,
# 	'high': 3.0 * 3.0 * 2,
# 	'alpha': 0.01,
# 	'max_modes': 3 }

# params = { 
# 	'algorithm': 'mean_bgs', 
# 	'low': 3 * 30 * 30,
# 	'high': 3 * 30 * 30 * 2,
# 	'alpha': 1e-6,
# 	'learning_frames': 30 }

# params = { 
# 	'algorithm': 'prati_mediod_bgs', 
# 	'low': 50,
# 	'high': 50 * 2,
# 	'weight': 1,
# 	'sampling_rate': 5,
# 	'history_size': 16 }

# params = { 
# 	'algorithm': 'wren_ga', 
# 	'low': 3.5 * 3.5,
# 	'high': 3.5 * 3.5 * 2,
# 	'alpha': 0.05,
# 	'learning_frames': 30 }

params = { 
	'algorithm': 'zivkovic_agmm', 
	'low': 5 * 5,
	'high': 5 * 5 * 2,
	'alpha': 0.001,
	'max_modes': 3 }

bg_sub = pybgs.BackgroundSubtraction()	
camera_source = cv2.VideoCapture("match1.mp4")
# camera_source.open(0)

i = 0
error, img = camera_source.read()
high_threshold_mask = np.zeros(shape=img.shape[0:2], dtype=np.uint8)
low_threshold_mask = np.zeros_like(high_threshold_mask)
bg_sub.init_model(img, params)

while cv2.waitKey(20) == -1:
    error, img = camera_source.read()
    # error, img2 = camera_source.read()
    # cv2.imshow('img1',img)
    # cv2.imshow('img2',img2)
    # delta=0
    # lower_gray = np.array([delta, delta,delta])
    # upper_gray = np.array([255-delta,255-delta,255-delta])
    # mask = cv2.inRange(img, lower_gray, upper_gray)
    # # res = cv2.bitwise_and(img,img, mask= mask)
    # HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # hue = HSV_img[:, :, 0]
    # hist = cv2.calcHist([hue],[0],None,[256],[0,256])
    # hist= hist[1:, :]
    # elem = np.argmax(hist)
    # tolerance = 0.15*elem
    # lower_gray = np.array([elem-tolerance, 0,0])
    # upper_gray = np.array([elem+tolerance,255,255])
    # mask = cv2.inRange(HSV_img, lower_gray, upper_gray)/255
    # cv2.imshow('ma',mask)
    # final_mask= get_mask(mask)
    # final_mask=np.array(final_mask)
    # final_mask = np.array(final_mask * 255, dtype = np.uint8) 
    # img = cv2.bitwise_and(img,img, mask= final_mask)
    # imgcp=img
    # blue=img[:,:,0]
    # green=img[:,:,1]
    # red=img[:,:,2]
    # for i in range (len(green)):
    # 	for j in range (len(green[0])):
    # 		if(green[i][j]>red[i][j] and red[i][j]>blue[i][j]):
    # 			continue
    # 		else:
    # 			imgcp[i][j]=0
    bg_sub.subtract(i, img, low_threshold_mask, high_threshold_mask)
    bg_sub.update(i, img, high_threshold_mask)
    # (cnts, _) = cv2.findContours(low_threshold_mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # for c in cnts:
    # 	# draw the contour and show i
    # 	cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    img = cv2.bitwise_and(img,img, mask= low_threshold_mask)
    # imgcp=img2
    # blue=img2[:,:,0]
    # green=img2[:,:,1]
    # red=img2[:,:,2]
    # for i in range (len(green)):
    # 	for j in range (len(green[0])):
    # 		if(green[i][j]>red[i][j] and red[i][j]>blue[i][j]):
    # 			continue
    # 		else:
    # 			imgcp[i][j]=0
    # imgcp = cv2.bitwise_and(imgcp,imgcp, mask= low_threshold_mask)
    cv2.imshow('mask', low_threshold_mask)
    cv2.imshow('foreground', img)
    # cv2.imshow('fore', imgcp)
    roi = img
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
    edges_frame = cv2.Canny(gray,255,250,apertureSize = 3)
    kernel = np.ones((3,3),np.uint8)
    closing = cv2.morphologyEx(edges_frame, cv2.MORPH_CLOSE,kernel, iterations=1)
    cont_img = closing.copy()
    contours, hierarchy = cv2.findContours(cont_img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
    	area = cv2.contourArea(cnt)
    	if area < 1 or area > 200:
    		continue
    	if len(cnt) < 5:
    		continue
    	M = cv2.moments(cnt)
    	cX = int(M["m10"] / M["m00"])
    	cY = int(M["m01"] / M["m00"])
    	dcolor=getColor(roi,cX,cY,30,200,250,200,250)
    	if(dcolor>1 and dcolor < 100):
    		cv2.circle(roi, (cX, cY), 7, (0, 0, 255), -1)
    	ellipse = cv2.fitEllipse(cnt)
    	cv2.ellipse(img, ellipse, (0,255,0), 2)
   
    cv2.imshow('Contours', roi)

    # cv2.imwrite('bgs.jpg',img)
    # cv2.imshow('background', bg_sub.get_background())
    i += 1

 
