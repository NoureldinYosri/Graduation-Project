#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:58:01 2017

@author: noureldin
"""

import cv2

class detector:
    def __init__(self):
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
        
    def detect(self,frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);
        found,weight = self.hog.detectMultiScale(frame, winStride=(4,4), padding=(32,32), scale=1.00005 , useMeanshiftGrouping = True);#hitThreshold,useMeanshiftGrouping
        if len(found) == 0: return [];
        return found;   
