# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys;
sys.path.insert(0, '../')
import joblib;
import nn_controller;
import cv2;
import logger;
from utils import *;
import time;
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pylab as plt
import numpy as np
import dimensionality_reduction;

def get_all_data(name_path):
    print('getting all data');
    for name,path in name_path:
        print ("started working on " + name + "'s data");
        start_time = time.time();
        X,Y = nn_controller.read_data(path);
        mylogger.save(X,'untransormed images of ' + name);
        mylogger.save(Y,'Ys of ' + name);
        elapsed_time = time.time() - start_time
        minutes = elapsed_time/60
        seconds = elapsed_time%60
        print ("finished working in %d min and %d seconds"%(minutes,seconds))
    

def save(obj,note,mylogger):
    print('started saving ',note);
    start_time = time.time();
    mylogger.save(obj,note);
    elapsed_time = time.time() - start_time
    minutes = elapsed_time/60
    seconds = elapsed_time%60
    print ("finished saving %s in %d min and %d seconds"%(note,minutes,seconds))

def load(path,note):
    print ('started loading ' ,note);
    start_time = time.time();
    ret = joblib.load(path);
    elapsed_time = time.time() - start_time
    minutes = elapsed_time/60
    seconds = elapsed_time%60
    print ("finished loading %s in %d min and %d seconds"%(note,minutes,seconds))
    return ret;
    
def split_into_batches(X,Y):
    BATCH_SIZE = 5000;
    Xs = [];
    Ys = [];
    s = 0;
    n = len(X);
    print('started spliting data of size',n);
    start_time = time.time();
    while s < n:
        e = min(s + BATCH_SIZE,n);
        Xs.append(X[s:e]);
        Ys.append(Y[s:e]);
        s = e;
    elapsed_time = time.time() - start_time
    minutes = elapsed_time/60
    seconds = elapsed_time%60
    print ("finished spliting data in %d min and %d seconds"%(minutes,seconds))
    return Xs,Ys;

def transorm_all():
    mylogger = logger.logger(join_parent('logger',2),'transforming all data');
    paths = ['/home/noureldin/Desktop/GP/used data/ball out','/home/noureldin/Desktop/GP/used data/goal','/home/noureldin/Desktop/GP/used data/kick','/home/noureldin/Desktop/GP/used data/pitch-invasion filtered','/home/noureldin/Desktop/GP/used data/vid_data_img_filtered'];
    name_path = [];
    for path in paths: name_path.append([path.split('/')[-1],path]);
    #get_all_data(name_path);
    
    surf_threshold = 4000;
    surf = cv2.xfeatures2d.SURF_create(surf_threshold)
    SOM = load('/home/noureldin/Desktop/workspace/logger/on Sun Jul  2 23-44-45 2017 SOM on all data with SURF threshold of 4000/1.pkl','SOM');
    path = '/home/noureldin/Desktop/workspace/ready to use/on Mon Jul  3 15-44-13 2017 transforming all data/%d.pkl';
    names = ['ball out','goal','kick','pitch-invasion','offenses'];
    for i in range(5):
        xpath = path%(2*i + 1);
        ypath = path%(2*i + 2);
        X = load(xpath,'Xs of ' + names[i]);
        Y = load(ypath,'Ys of ' + names[i]);
        Xs,Ys = split_into_batches(X,Y);
        tX = [];
        tY = [];
        print(len(Xs));
        for j in range(1,len(Xs) + 1):
            print('working on %s batch number %d of %d'%(names[i],j,len(Xs)));
            X,Y = nn_controller.transform_data(Xs[j-1],Ys[j-1],surf,SOM,50,50);
            tX.extend(X);
            tY.extend(Y);
        save(tX,'transformed Xs of ' + names[i],mylogger);
        save(tY,'transformed Ys of ' + names[i],mylogger);

        

def run_experiment(X,Y,hidden_layer_shape,PCA_attributes_size,PCA_whiten,mylogger = None,note = ""):
    if PCA_attributes_size is not None:
        X = dimensionality_reduction.reduce_pca(X,PCA_attributes_size,PCA_whiten);
    X_train,Y_train,X_test,Y_test = nn_controller.split(X,Y)
    clf = nn_controller.get_clf(X_train,Y_train,hidden_layer_shape)
    note += "hidden layer shape is " + str(hidden_layer_shape) + "\n";
    note += "PCA params are " + str(PCA_attributes_size) + " ," + str(PCA_whiten) ;
    nn_controller.do_statistical_work(X_train,Y_train,X_test,Y_test,clf,mylogger,note);

def create_humongous_data(path):
    X = [];
    Y = [];
    names = ['ball out','goal','kick','pitch-invasion','offenses'];
    offset = 0;
    for i in range(5):
        xpath = path%(2*i+1);
        ypath = path%(2*i+2);
        X.extend(load(xpath,'Xs of ' + names[i]));
        tY = load(ypath,'Ys of ' + names[i]);
        mx = max(tY);
        Y.extend(map(lambda x:x + offset,tY));
        offset += mx + 1;
    return X,Y;

if __name__ == "__main__":
    name = "offenses";
    names = ['ball out','goal','kick','pitch-invasion','offenses'];
    path = '/home/noureldin/Desktop/workspace/logger/on Mon Jul  3 17-06-38 2017 transforming all data/%d.pkl';
    mylogger = logger.logger(join_parent('logger',2),'getting all clfs');
#    for i in range(5):
#        xpath = path%(2*i+1);
#        ypath = path%(2*i+2);
#        X = load(xpath,'Xs of ' + names[i]);
#        Y = load(ypath,'Ys of ' + names[i]);
#        run_experiment(X,Y,(30,30,30),None,None,mylogger,'clf of ' + names[i] + "\n");
    path = '/home/noureldin/Desktop/workspace/logger/on Mon Jul  3 17-06-38 2017 transforming all data/%d.pkl';
    X,Y = create_humongous_data(path);
##    X = dimensionality_reduction.reduce_pca(X,1500,False);
#    run_experiment(X,Y,(30,30),None,None,mylogger=mylogger);
    for i in range(1,5+1):
        run_experiment(X,Y,(30,30,30),100 + i*20,False,mylogger,"clf of all\n");
    
    
    #create_humongous_network();
