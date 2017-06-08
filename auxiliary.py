#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 01:13:08 2017

@author: noureldin
"""

from os import walk
def get_all_file_paths(path):
    """gets addresses of all files in a path recusivly"""
    nxt = [];
    ret = [];
    for (dirpath, dirnames, filenames) in walk(path):
        ret.extend(map(lambda filename:path + "/" + filename,filenames));
        nxt = map(lambda dirname:path + "/" + dirname,dirnames);
        break
    for sub_path in nxt:
        ret.extend(get_all_file_paths(sub_path));
    return ret;


    