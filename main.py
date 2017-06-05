#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 18:10:05 2017

@author: noureldin
"""

# -*- coding: utf-8 -*-


import cv2
import sys
import detect_humans,track_humans;
import pitch_elemenation;


if __name__ == '__main__' :
    #reading video
    videoPath = "../gp_media/video.mp4"
    video = cv2.VideoCapture(videoPath)
     
    # Exit if video not opened.
    if not video.isOpened():
        print "Could not open video"
        sys.exit()
 
    #module instances
    detector = detect_humans.detector();
    tracker = None;
    backgroundsubtractor = cv2.bgsegm.createBackgroundSubtractorMOG()
 
    frame_idx = 0;
    while True:
        ok, frame = video.read();
        
        if not ok: break;
        print "processing frame #",frame_idx;
        
        #any preprocessing on the frame
        
        #frame = pitch_elemenation.remove_pitch(frame);
        #fgmask = backgroundsubtractor.apply(frame)
        #frame = cv2.bitwise_and(frame,frame,mask = fgmask)
 
        #detect or update tracker
        if frame_idx%70 == 0:
            detectedPeople = detector.detect(frame);
            tracker = track_humans.tracker(detectedPeople,frame);
        else:
            # Update tracker
            tracker.update_and_draw_box(frame);
                    
        #any postprocessing
        
        
        frame_idx += 1;
        cv2.imshow("Tracking", frame); 
        cv2.waitKey(3);
