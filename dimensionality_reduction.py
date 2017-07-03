#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:38:39 2017

@author: noureldin
"""
from sklearn.decomposition import PCA
import numpy as np;
import time;

def reduce_pca(X,n_attributes = 10,pca_whiten = False):
    print('started PCA');
    start_time = time.time();
    pca = PCA(n_components=n_attributes,whiten=pca_whiten);
    pca.fit(X);
    elapsed_time = time.time() - start_time
    minutes = elapsed_time/60
    seconds = elapsed_time%60
    print ("finished PCA in %d min and %d seconds"%(minutes,seconds))    
    #print (pca.explained_variance_ratio_);
    return pca.transform(X);

if __name__ == "__main__":
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    #print(reduce(X,1)); 