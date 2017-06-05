#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:09:57 2017

@author: noureldin
"""
import cv2;
import numpy as np;

def remove_pitch(img):
    blue =img[:,:,0]
    green=img[:,:,1]
    red=img[:,:,2]
    msk = 255 - (green > 120) * (green < 180) * (green > red) * (red > blue) * 255;
    msk = np.array(msk,dtype = np.uint8);
    img = cv2.bitwise_and(img,img,mask = msk);
    return img


if __name__ == "__main__":
    path = "../gp_media/testimage.jpg";
    img = cv2.imread(path);
    print img;
    cv2.imshow('img',remove_pitch(img));
    cv2.waitKey(0);
