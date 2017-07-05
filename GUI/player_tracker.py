#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:58:01 2017

@author: noureldin
"""
import cv2
from player_detector import detector as PlayerDetector

class tracker:
    def __init__(self,detected_people=None,frame=None):
        if detected_people and frame:
            init_trackers(detected_people, frame)
        self.cnt = 0;
        self.detector = PlayerDetector()

    def init_trackers(self, detected_people, frame):
        self.trackers = [cv2.Tracker_create("MIL") for person in detected_people] 
        for i in range(len(detected_people)):
            self.trackers[i].init(frame,tuple(detected_people[i]));

    def update_and_draw_box(self,frame):
        if self.cnt % 30 == 0:
            rectangles = self.detector.detect(frame)
            self.init_trackers(rectangles, frame)
        self.cnt += 1;
        for tracker in self.trackers:
            ok, bbox = tracker.update(frame)
            if ok:
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (0,0,255))
        return frame
