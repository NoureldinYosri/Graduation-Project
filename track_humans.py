#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:58:01 2017

@author: noureldin
"""
import cv2;

class tracker:
    def __init__(self,detected_people,frame):
        self.trackers = [cv2.Tracker_create("MIL") for person in detected_people]; 
        map(lambda tracker,box:tracker.init(frame,tuple(box)),self.trackers,detected_people);

    def update_and_draw_box(self,frame):
        for tracker in self.trackers:
            ok, bbox = tracker.update(frame);
            if ok:
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (0,0,255))
    
