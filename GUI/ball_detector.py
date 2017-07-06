import cv2, numpy as np, math

def eleminateCrowd(img):
	blue=img[:,:,0]
	green=img[:,:,1]
	red=img[:,:,2]
	row=len(green)
	col=len(green[0])
	for i in range (row):
		for j in range (col):
			if(green[i][j]>120 and  (green[i][j]>red[i][j] and red[i][j]>blue[i][j])):
				continue
			img[i][j]=0

	return img

def get_mask(I):
	"""takes a 2d msk array of 0s and 1s"""
	if len(I) == 0 or len(I[0]) == 0: return 0;
	n = len(I);
	m = len(I[0]);
	# for row in I:
	# 	if len(row) != m:
	# 		print "uneven dimensions ... aborting";
	# 		return;
	row_sum = [0 for i in range(n)];
	col_sum = [0 for i in range(m)];
	row_sum2 = [0 for i in range(n)];
	col_sum2 = [0 for i in range(m)];
	msk = [[0 for j in range(m)] for i in range(n)];
	for i in range(n):
		for j in range(m):
			col_sum[j] += I[i][j];
			row_sum[i] += I[i][j];
	for i in range(n):
		for j in range(m):
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

def eleminateCrowd2(img):
	delta=0
	lower_gray = np.array([delta, delta,delta])
	upper_gray = np.array([255-delta,255-delta,255-delta])
	mask = cv2.inRange(img, lower_gray, upper_gray)
	HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	hue = HSV_img[:, :, 0]
	hist = cv2.calcHist([hue],[0],None,[256],[0,256])
	hist= hist[1:, :]
	elem = np.argmax(hist)
	tolerance = 0.15*elem
	lower_gray = np.array([elem-tolerance, 0,0])
	upper_gray = np.array([elem+tolerance,255,255])
	mask = cv2.inRange(HSV_img, lower_gray, upper_gray)/255
	final_mask= get_mask(mask)
	final_mask=np.array(final_mask)
	final_mask = np.array(final_mask * 255, dtype = np.uint8) 
	img = cv2.bitwise_and(img,img, mask= final_mask)
	return img

def morphoImg(img):

	# edge detection
	edges = cv2.Canny(img,255,250,apertureSize = 3)
	
	# closing
	kernel = np.ones((5,5),np.uint8) 
	closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
	# dilation
	kernel = np.ones((5,5),np.uint8)
	dilation = cv2.dilate(closing,kernel,iterations = 1)

	erosion = cv2.erode(dilation,kernel,iterations = 1)
	return erosion

def eleminateBallCandidate(cnt , colorImg):
	rect = cv2.minAreaRect(cnt)
	box = cv2.boxPoints(rect)
	width = math.hypot(box[1][0] - box[0][0], box[1][1] - box[0][1])
	height = math.hypot(box[2][0] - box[1][0], box[2][1] - box[1][1])
	axes1 = math.hypot(box[2][0] - box[0][0], box[2][1] - box[1][1])
	axes2 = math.hypot(box[1][0] - box[3][0], box[1][1] - box[3][1])
	minX = 10000
	minY = 10000
	maxX = 0
	maxY = 0
	for i in range(0, 3):
		for j in range(0, 1):
			minX = int(min(minX, box[i][1]))
			minY = int(min(minY, box[i][0]))
			maxX = int(max(maxX, box[i][1]))
			maxY = int(max(maxY, box[i][0]))
	whRatio = height / width
	axRatio = axes1 / axes2
	if (whRatio < 0.5 or whRatio > 1.3) or (axRatio < 0.6 or axRatio > 1.1):
		return [-1,-1];
	count = 0
	# print(maxX , maxY)
	if(maxX>720):
		maxX=720
	for i in range(minX, maxX):
		for j in range(minY, maxY):
			if (colorImg[i,j,1] > 190 and colorImg[i,j,2] > 190):
				count += 1

	return [count,box]

def findBall(img , colorImg):
	im2, contours, hierarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE )
	for cnt in contours:
		area = cv2.contourArea(cnt)
		if area < 5 or area > 200:
			continue
		cou = eleminateBallCandidate(cnt,colorImg)
		if(cou[0] == -1):
			continue
		count = cou[0]
		box = cou[1]
		if count < 8:
			continue
		box = np.int0(box)
		cv2.drawContours(colorImg,[box],0,(0,0,255),2)
	
	return colorImg

def start_detecting(path):
	camera_source = cv2.VideoCapture(path)
	while True:
		error, img = camera_source.read()
		colorImg = img
		img = morphoImg(img)
		img = findBall(img, colorImg)
		cv2.imshow('Ball Tracking', img)
		
		if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

if __name__ == '__main__':
	start_detecting("bb.mp4")

