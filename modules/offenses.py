#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 03:15:08 2017

@author: noureldin
"""

import nn_controller

def train(path):
    nn_controller.conduct_experiment(path,[40,40],[30,30,30],5000,"offenses");

if __name__ == "__main__":
    path = '/home/noureldin/Desktop/GP/dataset/vid_data_img_filtered';
    train(path);