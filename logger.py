#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 00:58:44 2017

@author: noureldin
"""

import os,time,joblib;

class logger:
    def __init__(self,path,note = None):
        self.path = path;
        if not path.endswith('/'): self.path += "/";
        if note != None: self.path += note;
        self.path += " on " + time.ctime();
        try:
            os.makedirs(self.path)
        except:
            pass;
        self.cnt = 0;
    
    def save(self,obj,message = ""):
        self.cnt += 1;
        joblib.dump(obj,self.path + '/' + str(self.cnt) + ".pkl");
        f = file(self.path + '/' + "note on trial #%d.txt"%self.cnt,"w");
        f.write(message);
        f.close();
  
    
