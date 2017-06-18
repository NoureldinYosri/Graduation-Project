#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 00:58:44 2017

@author: noureldin
"""

import os,time,joblib,re;
from utils import *
from enum import Enum

class Log(Enum):
     SOM = "1"
     IMGS = "2"
     LABELS = "3"
     CLF = "4"

class logger:
    def __init__(self,path,note = None):
        self.path = path;
        folder_name = "on " + str(time.ctime());
        if note != None: folder_name += " " + note;
        self.path = join(path,folder_name);
        self.path = normalize_dir(self.path)
#        print(self.path)
        try:
            os.makedirs(self.path)
        except:
            pass;
        self.cnt = 0;
    
    def save(self,obj,message = ""):
        self.cnt += 1;
        joblib.dump(obj, join(self.path, str(self.cnt) + ".pkl"));
        file_path = join(self.path, "note on trial #%d.txt"%self.cnt)
        f = open(file_path, "w");
        f.write(message);
        f.close();