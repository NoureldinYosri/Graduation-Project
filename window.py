#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:08:59 2017

@author: noureldin
"""

import Queue;

class window:
    
    def __init__(self,iclfs,window_size):
        self.q = Queue.Queue();
        self.iclfs = iclfs;        
        self.freq = {};
        self.window_size = window_size;
        
    def get_classes(self,feature_vector):
        ret = [];
        for clf in self.iclfs:
            y = clf.predict(feature_vector);
            ret.append(y);
        return ret;
    
    def add(self,feature_vector):
        classes = self.get_classes(feature_vector);
        self.q.put(classes);
        for y in classes:
            if y not in self.freq: self.freq[y] = 0;
            self.freq[y] += 1;
        if self.q.qSize() > self.window_size:
            classes = self.q.get();
            for y in classes:
                self.freq[y] -= 1;
    
    def get_events(self):
        mx = 0;
        for y in self.freq:
            mx = max(mx,self.freq[y]);
        if mx == 0: return [];
        ret = [];
        for y in self.freq:
            if self.freq[y] == mx:
                ret.append(y);
        if "nothing" in ret: return [];
        return ret;