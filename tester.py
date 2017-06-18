import joblib,cv2;
import somoclu;
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import numpy as np;
import utils
from logger import *

def assign_vals(labels):
    label_val = {}
    cur = 0
    for label in labels:
        label_val[label] = cur
        cur += 1
    return label_val

def read_data(path):
    """returns path X,Y of data where X[i] is an image and Y[i] is its label"""
    data = {}
    val = {"no":-1,"undetermined":0,"yes":1}
    print ("started reading data")
    start_time = time.time()
    labels = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        labels.extend(dirnames)
        break
    label_val = assign_vals(labels)
    for (dirpath, dirnames, filenames) in os.walk(path):
        	label = utils.get_dirname(dirpath)
        	if label not in label_val: 
        		continue
        	data[label] = filenames
    X = []
    Y = []
    for label in data:
        for img_name in data[label]:
            path_to_img = utils.join_list([path, label, img_name])
            X.append(cv2.imread(path_to_img,0))
            Y.append(label_val[label])
    elapsed_time = time.time() - start_time
    minutes = elapsed_time/60
    seconds = elapsed_time%60
    print ("finished reading data in %d min and %d seconds"%(minutes,seconds))
    X = np.array(X)
    Y = np.array(Y)
    return X,Y

def transform_data(imgs,labels,som,m,n):
    data = zip(imgs, labels)
    res_imgs = []
    res_labels = []
    surf = cv2.xfeatures2d.SURF_create(10000)
    print ("started transforming data")
    cnt = 0
    start_time = time.time()
    for img, label in data:
        kp, des = surf.detectAndCompute(img,None)
        if des is None: continue
        compressed = [0 for i in range(m*n)]
        for feature_description in des:
            cnt += 1
            activation_map = som.get_surface_state(np.array(feature_description).reshape(1,64))
            for match in som.get_bmus(activation_map):
                compressed[match[0]*n + match[1]] += 1
        res_imgs.append(np.array(compressed,dtype = np.float32))
        res_labels.append(label)

    elapsed_time = time.time() - start_time
    minutes = elapsed_time/60
    seconds = elapsed_time%60
    print ("finished transforming %d features in %d min and %d seconds"%(cnt,minutes,seconds))
    return res_imgs, res_labels

def test(imgs,labels,path_to_trained_som,path_to_trained_network,som_m,som_n):
	surf = cv2.xfeatures2d.SURF_create(10000);
	print ('reading som');
	som = joblib.load(path_to_trained_som);
	print ('reading network')
	clf = joblib.load(path_to_trained_network);
	print ("found %d images" % (len(imgs)))
	print ('compressing images');
	imgs, labels = transform_data(imgs, labels, som, som_m, som_n)
	prediction = clf.predict(imgs);
	accuracy = accuracy_score(labels, prediction)*100;
	return accuracy;

if __name__ == "__main__":
	# ToDo: change the logger child directory to reflect the right cached SOM
	dir_list = ['..', 'logger', 'on Sun Jun 18 04-04-03 2017 working on goal with MLP and SOM is [20, 20] and [5, 5] hidden layer']
	som_path = utils.join_list(dir_list + [Log.SOM.value+".pkl"])
	NN_path = utils.join_list(dir_list + [Log.CLF.value+".pkl"])
	data_path = utils.join_parent("goal") #ToDo: use the testing data path instead
	imgs, labels = read_data(data_path)
	print (test(imgs,labels,som_path,NN_path,20,20))
