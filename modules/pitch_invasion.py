# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nn_controller

def train(path):
    surf_threshold = 4000;
    nn_controller.conduct_experiment(path,[30,30],[30,30],surf_threshold,"pitch invasion");


if __name__ == "__main__":
    path = '/home/noureldin/Desktop/GP/dataset/pitch-invasion filtered';
    train(path);