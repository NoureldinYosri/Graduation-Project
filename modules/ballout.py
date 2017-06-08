#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:25:20 2017

@author: noureldin
"""

import tensorflow as tf
import cv2,time;
from os import walk
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import sys,random
import matplotlib.pylab as plt;

sys.path.insert(0, '../')
import logger,SOM;

def read_data(path):
    """returns path X,Y of data where X[i] is an image and Y[i] is its label"""
    data = {};
    val = {"no":-1,"undetermined":0,"yes":1};
    
    for (dirpath, dirnames, filenames) in walk(path):
        label = dirpath.split('/')[-1];
        if label not in ["no","yes","undetermined"]: continue;
        data[label] = filenames;
        
    X = [];
    Y = [];
    cnt = [0 for i in xrange(3)];
    for label in data:
        for img_name in data[label]:
            path_to_img = path+"/" +label+"/"+img_name;
            X.append(cv2.imread(path_to_img,0));
            Y.append(val[label]);
            cnt[val[label]+1] += 1;
    X = np.array(X);
    Y = np.array(Y);
    return X,Y,cnt;

def transform_data(imgs,som,m,n):
    X = [];
    surf = cv2.xfeatures2d.SURF_create(10000)
    print "started transforming data";
    cnt = 0;
    start_time = time.time();
    for img in imgs:
        kp, des = surf.detectAndCompute(img,None)
        if des is None: continue;
        compressed = [0 for i in xrange(m*n)];
        for feature_description in des:
            cnt += 1;
            activation_map = som.get_surface_state(np.array(feature_description).reshape(1,64));
            for match in som.get_bmus(activation_map):
                compressed[match[0]*n + match[1]] += 1;
        X.append(np.array(compressed,dtype = np.float32));
    elapsed_time = time.time() - start_time;
    minutes = elapsed_time/60;
    seconds = elapsed_time%60;
    print "finished transforming %d features in %d min and %d seconds"%(cnt,minutes,seconds);
    return X;
   
if __name__ == "__main__":
    mylogger = logger.logger('/home/noureldin/Desktop/workspace/logger','working on ballout with MLP and SOM is 30*30 and 5*5 hidden layer');
    path = "/home/noureldin/Desktop/GP/dataset/BFC VS MAG";
    print "reading data";
    X,Y,label_sizes = read_data(path);
    print "done reading";
    path = '/home/noureldin/Desktop/GP/dataset/BFC VS MAG'
    som = SOM.train(path,30,30);
    X = transform_data(X,som,30,30);
    print "start training MLP";
    start_time = time.time();
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,5), random_state=1)
    X_train = [];
    X_test = [];
    Y_train = [];
    Y_test = [];
    offset = 0;
    for i in xrange(3):
        x_train, x_test, y_train, y_test =  \
                        train_test_split(X[offset:offset+label_sizes[i]], Y[offset:offset+label_sizes[i]], test_size=0.3, random_state=42)
        X_train.extend(x_train);
        X_test.extend(x_test);
        Y_train.extend(y_train);
        Y_test.extend(y_test);
        offset += label_sizes[i];
    X_train = np.array(X_train,dtype = np.float32);
    X_test = np.array(X_test,dtype = np.float32);
    Y_train = np.array(Y_train,dtype = np.float32);
    Y_test = np.array(Y_test,dtype = np.float32);
    clf.fit(X_train,Y_train);
    elapsed_time = time.time() - start_time;
    minutes = elapsed_time/60;
    seconds = elapsed_time%60;
    print "finished learning in %d min and %d seconds"%(minutes,seconds);
    train_acc = accuracy_score(Y_train, clf.predict(X_train))*100;
    Y_predict = clf.predict(X_test);
    test_acc = accuracy_score(Y_test, Y_predict)*100;
    baseline_acc = sum(Y_test == 1)*100.0/len(Y_test);
    print Y_test[:10],Y_predict[:10];
    print "training accuracy is %.10f ,test accuracy is %.10f ,baseline_acc is %.10f"%(train_acc,test_acc,baseline_acc);
    plt.hist(np.array(clf.predict(X_test)));
    plt.show();
    plt.savefig('histogram of predictions using 30*30 SOM shot number 1 wit 5*5 hidden layer.jpg');
    error_matrix = [[0 for i in xrange(3)] for j in xrange(3)];
    for i in xrange(3):
        for j in xrange(3):
            error_matrix[i][j] = sum(np.array(Y_test==(i-1)) * np.array(Y_predict==(j-1)));
    print error_matrix;
    mylogger.save(clf,'MLP model training accuracy is %.10f ,test accuracy is %.10f ,baseline_acc is %.10f'%(train_acc,test_acc,baseline_acc) + "\n error matrix contains " + str(error_matrix) );
    