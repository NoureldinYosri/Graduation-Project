#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:25:20 2017

@author: noureldin
"""

import tensorflow as tf
import cv2,random
from os import walk
import numpy as np

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
    
    for label in data:
        for img_name in data[label]:
            path_to_img = path+"/" +label+"/"+img_name;
            X.append(cv2.imread(path_to_img,0));
            Y.append(val[label]);
    X = np.array(X);
    Y = np.array(Y);
    return X,Y;

def preprocess(X,Y):
    factory = cv2.xfeatures2d.SURF_create(4000)
    nX = map(lambda img:factory.detectAndCompute(img,None)[0],X);
#    img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
    #cv2.imshow('with features',img2);
    #cv2.waitKey(0);
    #np.matrix(nX,Y);
    return nX,Y;
   
if __name__ == "__main__":
    path = "/home/noureldin/Desktop/GP/dataset/BFC VS MAG";
    print "reading data";
    X,Y = read_data(path);
    print "done reading";
    print "preprocessing data";
    X,Y = preprocess(X,Y);
    print "done preprocessing";
    
    print dir(X[0][0]);