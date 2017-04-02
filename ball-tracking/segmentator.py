import numpy as np, cv2 , pymeanshift as pms
img=cv2.imread('sample3.jpg')
(segmented_image, labels_image, number_regions) = pms.segment(img, spatial_radius=2,range_radius=4, min_density=10)
print (number_regions)
cv2.imwrite("Ss3.jpg", segmented_image)
# meanshift = cv2.pyrMeanShiftFiltering(segmented_image, sp=8, sr=16, maxLevel=1, termcrit=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 5, 1))
cv2.imshow('image',segmented_image)

cv2.waitKey(0)
