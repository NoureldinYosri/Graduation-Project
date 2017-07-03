#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:36:59 2017

@author: noureldin
"""

import joblib;
import numpy as np;

class iclf:
    def __init__(self,clf,interpretation,name):
        self.clf = clf if type(clf) != type("") else joblib.load(clf);
        self.interpretation = interpretation;
        self.name = name;
    
    def predict(self,feature_vector):
        #X = [feature_vector,feature_vector];
        sh = len(feature_vector);
        X = np.array([feature_vector]).reshape(1,sh);
        y = self.clf.predict(X);
        y = int(y);
        if y not in self.interpretation: 
            raise Exception(str(y) + " not in interpretation of " + self.name);
        else: 
            return self.interpretation[y];
        
        
if __name__ =="__main__":
    path = '/home/noureldin/Desktop/workspace/logger/on Sat Jun 24 16-23-56 2017 working on pitch invasion with MLP and SOM is [30, 30] and [30, 30] hidden layer/4.pkl';
    intr = {0:"nothing",1:"pitch invasion"};
    my_iclf = iclf(path,intr,"pitch invasion");
    clf = joblib.load(path);
    path = '/home/noureldin/Desktop/workspace/logger/on Sat Jun 24 16-23-56 2017 working on pitch invasion with MLP and SOM is [30, 30] and [30, 30] hidden layer/2.pkl'
    X = joblib.load(path);
    Y = joblib.load('/home/noureldin/Desktop/workspace/logger/on Sat Jun 24 16-23-56 2017 working on pitch invasion with MLP and SOM is [30, 30] and [30, 30] hidden layer/3.pkl');
    for i in range(10):
        print (my_iclf.predict(X[i]),Y[i]);
    