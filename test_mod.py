import cv2
import numpy as np
import joblib
import somoclu
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import utils
from logger import *
from tester import *

def nn_mod(img, som, clf, surf):
	img = transform_data(img, som, surf, 20, 20)
	prediction = clf.predict(img);
	print(int(prediction[0]))

def transform_data(img,som,surf,m,n):
	cnt = 0
	kp, des = surf.detectAndCompute(img,None)
	# print (des)
	compressed = [0 for i in range(m*n)]
	for feature_description in des:
		cnt += 1
		activation_map = som.get_surface_state(np.array(feature_description).reshape(1,64))
		for match in som.get_bmus(activation_map):
			compressed[match[0]*n + match[1]] += 1
	res_img = np.array(compressed,dtype = np.float32)
	return res_img

if __name__ == "__main__":	
	camera = cv2.VideoCapture(utils.join_parent('vid.mp4'))
	dir_list = ['..', 'logger', 'on Sun Jun 18 13-53-06 2017 working on goal with MLP and SOM is [20, 20] and [5, 5] hidden layer']
	som_path = utils.join_list(dir_list + [Log.SOM.value+".pkl"])
	NN_path = utils.join_list(dir_list + [Log.CLF.value+".pkl"])
	som = joblib.load(som_path)
	clf = joblib.load(NN_path)
	surf = cv2.xfeatures2d.SURF_create(11000)
	while True:
		ret, img = camera.read()
		# kp, des = surf.detectAndCompute(img,None)
		# print(des)
		# cv2.imshow('vid', img)
		# img = np.array(img)
		cv2.imshow('video', img)
		nn_mod(img, som, clf, surf)
		if cv2.waitKey(1) & 0xFF == ord('q'):
	            break