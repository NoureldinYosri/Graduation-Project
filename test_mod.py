import cv2
import numpy as np
import joblib
import somoclu
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import utils
from logger import *
from tester import *

def nn_mod(img):
	dir_list = ['..', 'logger', 'on Sun Jun 18 13-53-06 2017 working on goal with MLP and SOM is [20, 20] and [5, 5] hidden layer']
	som_path = utils.join_list(dir_list + [Log.SOM.value+".pkl"])
	NN_path = utils.join_list(dir_list + [Log.CLF.value+".pkl"])
	som = joblib.load(som_path);
	clf = joblib.load(NN_path);
	img = transform_data(img, som, 20, 20)
	prediction = clf.predict(img);
	print(prediction)

def transform_data(img,som,m,n):
    surf = cv2.xfeatures2d.SURF_create(11000)
    cnt = 0
    kp, des = surf.detectAndCompute(img,None)
    compressed = [0 for i in range(m*n)]
    for feature_description in des:
        cnt += 1
        activation_map = som.get_surface_state(np.array(feature_description).reshape(1,64))
        for match in som.get_bmus(activation_map):
            compressed[match[0]*n + match[1]] += 1
    res_img = np.array(compressed,dtype = np.float32)
    return res_img

if __name__ == "__main__":	
	camera = cv2.VideoCapture('..\\vid.mp4')
	while True:
		ret, img = camera.read()
		surf = cv2.xfeatures2d.SURF_create(11000)
		kp, des = surf.detectAndCompute(img,None)
		print(des)
		# cv2.imshow('vid', img)
		# img = np.array(img)
		# nn_mod(img)
		if cv2.waitKey(1) & 0xFF == ord('q'):
	            break