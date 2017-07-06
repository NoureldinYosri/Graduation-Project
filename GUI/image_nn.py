import cv2, sys
import numpy as np
import joblib
import somoclu
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
sys.path.append("..")
import utils
from logger import *

class ImageClassifier:
    def __init__(self):
        self.som, self.clf = self.get_som_clf()

    def get_som_clf(self):
        dir_list = ['..', '..', 'logger', 'final']
        som_path = utils.join_list(dir_list + [Log.FINAL_SOM.value+".pkl"])
        NN_path = utils.join_list(dir_list + [Log.FINAL_CLF.value+".pkl"])
        som = joblib.load(som_path)
        clf = joblib.load(NN_path)
        return som, clf

    def classify(self, img):
        img = self.transform_data(img, self.som)
        prediction = self.clf.predict(np.array([img]))
        return int(prediction[0])

    def transform_data(self, img, som, m=50, n=50):
        cnt = 0
        surf = cv2.xfeatures2d.SURF_create(4000)
        kp, des = surf.detectAndCompute(img,None)
        # print (des)
        compressed = [0 for i in range(m*n)]
        if des != None:
            for feature_description in des:
                cnt += 1
                activation_map = som.get_surface_state(np.array(feature_description).reshape(1,64))
                for match in som.get_bmus(activation_map):
                    compressed[match[0]*n + match[1]] += 1
        res_img = np.array(compressed,dtype = np.float32)
        return res_img