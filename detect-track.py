#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:10:05 2017

@author: noureldin
"""

# -*- coding: utf-8 -*-


import numpy as np
import cv2
import sys
videoPath = "../gp_media/video.mp4"


def update_and_draw_box(tracker):
    ok, bbox = tracker.update(frame);
    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0,0,255))


hog = cv2.HOGDescriptor()
hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
def detect(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV);
    found,weight=hog.detectMultiScale(frame, winStride=(8,8), padding=(32,32), scale=1.001 , useMeanshiftGrouping = False);#hitThreshold,useMeanshiftGrouping
    #draw_detections(frame,found)
    if len(found) == 0: return [];
    return found;   
    


if __name__ == '__main__' :
    video = cv2.VideoCapture(videoPath)
     
    # Exit if video not opened.
    if not video.isOpened():
        print "Could not open video"
        sys.exit()
 
     
    trackers = None;
    frame_idx = 0;
    while True:
        ok, frame = video.read();

        if not ok: break;
        print "processing frame #",frame_idx;
        
        if frame_idx%70 == 0:
            detectedPeople = detect(frame);
            trackers = [cv2.Tracker_create("MIL") for person in detectedPeople]; 
            map(lambda tracker,box:tracker.init(frame,tuple(box)),trackers,detectedPeople);
        else:
            # Update tracker
            map(update_and_draw_box,trackers);
                    
        frame_idx += 1;
        cv2.imshow("Tracking", frame); 
        cv2.waitKey(3);
