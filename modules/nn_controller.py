#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:25:20 2017

@author: noureldin
"""

#import tensorflow as tf
import cv2,time,sys
from os import walk
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import sys,random
import matplotlib.pylab as plt

sys.path.insert(0, '../')
import SOM,utils
from logger import *

def assign_vals(labels):
    label_val = {}
    val_label = {};
    cur = 0
    labels.sort();
    for label in labels:
        label_val[label] = cur
        val_label[cur] = label;
        cur += 1
    print ("val_label is ",val_label);
    return label_val

def read_data(path):
    """returns path X,Y of data where X[i] is an image and Y[i] is its label"""
    data = {}
    print ("started reading data")
    start_time = time.time()
    labels = []
    for (dirpath, dirnames, filenames) in walk(path):
        labels.extend(dirnames)
        break
    label_val = assign_vals(labels)
    cnt_all = 0;
    for (dirpath, dirnames, filenames) in walk(path):
        label = utils.get_dirname(dirpath)
        if label not in label_val: continue
        data[label] = filenames
        cnt_all += len(filenames);
    X = []
    Y = []
    cnt = lst = 0;
    for label in data:
        for img_name in data[label]:
            path_to_img = utils.join_list([path, label, img_name])
            X.append(cv2.imread(path_to_img,0))
            Y.append(label_val[label])
            cnt += 1;
            p = int(cnt*100.0/cnt_all);
            if p == lst + 5:
                print('%d%% done'%p,cnt);
                lst = p;
    
    elapsed_time = time.time() - start_time
    minutes = elapsed_time/60
    seconds = elapsed_time%60
    print ("finished reading data in %d min and %d seconds"%(minutes,seconds))
    #X = np.array(X)
    Y = np.array(Y)
    return X,Y

def transform_data(imgs,labels,surf,som,m,n):
    data = zip(imgs, labels)
    res_imgs = []
    res_labels = []
    print ("started transforming data")
    cnt = 0
    start_time = time.time()
    cnt = lst = 0;
    N = len(imgs);
    for img, label in data:
        kp, des = surf.detectAndCompute(img,None)
        cnt += 1;
        compressed = [0 for i in range(m*n)]
        if des is not None:
            #print('image %d of %d has %d features'%(cnt,N,len(des)));
            for feature_description in des:
                activation_map = som.get_surface_state(np.array(feature_description).reshape(1,64))
                for match in som.get_bmus(activation_map):
                    compressed[match[0]*n + match[1]] += 1
        res_imgs.append(np.array(compressed,dtype = np.float32))
        res_labels.append(label)
        p = int(cnt * 100.0/N);
        if p == lst + 5:
            print ('%d%% done'%p);
            lst = p;
    elapsed_time = time.time() - start_time
    minutes = elapsed_time/60
    seconds = elapsed_time%60
    print ("finished transforming %d features in %d min and %d seconds"%(cnt,minutes,seconds))
    return res_imgs, res_labels

def get_som(path,som_m,som_n,surf):
    som = SOM.train(path,som_m,som_n,surf)
    return som

def get_clf(X,Y,hidden_layer_shape):
    print ("start training MLP")
    start_time = time.time()
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=tuple(hidden_layer_shape), random_state=1)
    clf.fit(X,Y)
    elapsed_time = time.time() - start_time
    minutes = elapsed_time/60
    seconds = elapsed_time%60
    print ("finished learning in %d min and %d seconds"%(minutes,seconds))
    return clf    
   

def split(X,Y,testSize = 0.3):
    X_train, X_test, Y_train, Y_test =  \
									train_test_split(X, Y, test_size=0.3, random_state=42,stratify = Y)
    X_train = np.array(X_train,dtype = np.float32)
    X_test = np.array(X_test,dtype = np.float32)
    Y_train = np.array(Y_train,dtype = np.float32)
    Y_test = np.array(Y_test,dtype = np.float32)
    return X_train,Y_train,X_test,Y_test

def create_error_matrix(Y_true,prediction,note=""):
    vals = list(set(Y_true));
    n = len(vals);
    error_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            error_matrix[i][j] = sum(np.array(Y_true==vals[i]) * np.array(prediction==vals[j]));  

    fig, axes = plt.subplots(nrows=n);
    for i in range(n):
        axes[i].imshow([error_matrix[i]],cmap='hot',vmin = 0,vmax = sum(error_matrix[i]));
    plt.savefig(note + ' error_matrix.png')
    #plt.show();
    return error_matrix;

def get_most_frequent(Y):
    freq = {};
    max_freq = 0;
    for x in Y:
        if x not in freq: freq[x] = 0;
        freq[x] += 1;
        max_freq = max(max_freq,freq[x]);
    for x in freq:
        if freq[x] == max_freq:
            return x;
    return 0;


def do_statistical_work(X_train,Y_train,X_test,Y_test,clf,mylogger = None,note = ""):
    train_acc = accuracy_score(Y_train, clf.predict(X_train))*100
    Y_predict = clf.predict(X_test)
    test_acc = accuracy_score(Y_test, Y_predict)*100
    baseline_acc = sum(Y_test == get_most_frequent(Y_train))*100.0/len(Y_test)
    print ("training accuracy is %.10f, test accuracy is %.10f, baseline_acc is %.10f"%(train_acc,test_acc,baseline_acc))
    plt.hist(np.array(clf.predict(X_test)))
    plt.savefig(note + ' histogram.png')
    #plt.show()
    error_matrix = create_error_matrix(Y_test,Y_predict,note);
    print (error_matrix)
    if mylogger is not None: mylogger.save(clf,'MLP model training accuracy is %.10f, test accuracy is %.10f, baseline_acc is %.10f'%(train_acc,test_acc,baseline_acc) + "\n error matrix contains " + str(error_matrix) + "\n" + note)    


def conduct_experiment(path,som_shape,hidden_layer_shape,surf_threshold,module_name,som_path = None):
    mylogger = logger(utils.join_parent('logger', 2),'working on %s with MLP and SOM is %s and %s hidden layer'%(module_name,str(som_shape),str(hidden_layer_shape)))
    X,Y = read_data(path)
    surf = cv2.xfeatures2d.SURF_create(surf_threshold)
    if som_path is None: 
        som = get_som(path,surf,som_shape[0],som_shape[1])
        mylogger.save(som, Log.SOM.name)
    else: som = joblib.load(som_path);
    X,Y = transform_data(X,Y,surf,som,som_shape[0],som_shape[1])
    mylogger.save(X, Log.IMGS.name)
    mylogger.save(Y, Log.LABELS.name)
    X_train,Y_train,X_test,Y_test = split(X,Y)
    clf = get_clf(X_train,Y_train,hidden_layer_shape)
    mylogger.save(clf, Log.CLF.name)
    do_statistical_work(X_train,Y_train,X_test,Y_test,clf,mylogger);
    
if __name__ == "__main__":
    path = utils.join_parent("BFC VS MAG", 2)
    conduct_experiment(path,[20,20],[5,5],4000,"BFC VS MAG")