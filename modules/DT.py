# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import joblib
from modules import nn_controller
import numpy as np;
import time,sys;
sys.path.insert(0, '../')
import logger, utils

def read_data(path):
    X = [];
    Y = [];
    offset = 0;
    for i in range(1,5 + 1):
        xpath = path + str(2*i - 1) + ".pkl";
        ypath = path + str(2*i) + ".pkl";
        X.extend(joblib.load(xpath));
        tY = joblib.load(ypath); 
        Y.extend(map(lambda x:x + offset,tY));
        offset += max(tY) + 1;
    return X,Y;
    
def read_clfs(path):
    clfs = [None for i in range(6)];
    for i in range(1,6 + 1):
        clfs[i-1] = joblib.load(utils.join(path, str(i)+".pkl"));
    
    fclf = joblib.load(utils.join(path, "fclf.pkl"))
    return clfs, fclf;
    
    
def create_new_date(X,Y,clfs):
    print('started creating new data');
    start_time = time.time();
    for i in range(len(Y)):
        if Y[i] in [2,5,9,12]:
            Y[i] = 2;
    nX = [None for _ in range(len(X))];
    for i in range(len(X)):
        x = np.array([X[i]])
        nX[i] = [clfs[j].predict(x)[0] for j in range(len(clfs))];
    elapsed_time = time.time() - start_time;
    m = elapsed_time/60;
    s = elapsed_time%60;
    print('finished in %d min and %d sec'%(m,s));
    return nX,Y;
    

class classifier:
    def __init__(self,clfs,fclf):
        self.clfs = [clf for clf in clfs];
        self.fclf = fclf;
    def predict(self,x):
        x = np.array([x]);
        x = [clf.predict(x)[0] for clf in self.clfs];
        x = np.array([x]);
        return int(self.fclf.predict(x)[0]);
        
if __name__ == "__main__":
#    path = '/home/islam/Desktop/drive-download-20170705T193213Z-001/on Mon Jul  3 21-41-53 2017 getting all clfs/';
#    clfs = read_clfs(path);
#    path = '/home/islam/Desktop/drive-download-20170705T193213Z-001/on Mon Jul  3 17-06-38 2017 transforming all data/';
#    X,Y = read_data(path);
#    X,Y = create_new_date(X,Y,clfs);
#    X = np.array(X);
#    Y = np.array(Y);
    hidden_layer_shape = (100,100,100);    
    Log = logger.logger("/home/islam/Desktop/logger","new clfs " + str(hidden_layer_shape));
#    Log.save(X,'new Xs');
#    Log.save(Y,'new Ys');
    X = joblib.load('/home/islam/Desktop/logger/on Wed Jul  5 22-14-58 2017 new data/1.pkl');
    Y = joblib.load('/home/islam/Desktop/logger/on Wed Jul  5 22-14-58 2017 new data/2.pkl');
    
    X_train,Y_train,X_test,Y_test = nn_controller.split(X,Y,Log);
    clf = nn_controller.get_clf(X_train,Y_train,hidden_layer_shape);
    nn_controller.do_statistical_work(X_train,Y_train,X_test,Y_test,clf);
    Log.save(clf,'clf');