import joblib,cv2;
import somoclu;
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import numpy as np;
from utils import *

def compress_image(img_path,som,surf,som_m,som_n):
	img = cv2.imread(img_path);
	kp, des = surf.detectAndCompute(img,None);
	compressed = [0 for i in range(som_m*som_n)];
	if des is not None: 
		for feature_description in des:
			activation_map = som.get_surface_state(np.array(feature_description).reshape(1,64));
			for match in som.get_bmus(activation_map):
				compressed[match[0]*som_n + match[1]] += 1;
	return np.array(compressed,dtype = np.float32);


def tester(list_of_new_images_paths,correct_labels,path_to_trained_som,path_to_trained_network,som_m,som_n):
	surf = cv2.xfeatures2d.SURF_create(10000);
	print ('reading som');
	som = joblib.load(path_to_trained_som);
	print ('reading network')
	clf = joblib.load(path_to_trained_network);
	print ('compressing images');
	n = len(list_of_new_images_paths);
	X = [];
	for i in range(n):
		X.append(compress_image(list_of_new_images_paths[i],som,surf,som_m,som_n));
	X = np.array(X,dtype = np.float32);
	prediction = clf.predict(X);
	accuracy = accuracy_score(correct_labels, prediction)*100;
	return accuracy;

if __name__ == "__main__":
	# ToDo: change the logger child directory to reflect the right cached SOM
	dir_list = ['..', 'logger', 'on Sun Jun 11 23:43:37 2017 working on ballout with MLP and SOM is 50x50 and 30x30 hidden layer with merged data set'];
	som_path = join_list(dir_list + ['1.pkl'])
	NN_path = join_list(dir_list + ['4.pkl'])
	print (som_path, NN_path)
	img_paths = [];
	correct_labels = [1];
	print (tester(img_paths,correct_labels, som_path,NN_path,50,50));
