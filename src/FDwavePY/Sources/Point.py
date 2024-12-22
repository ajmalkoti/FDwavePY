#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 11:23:05 2024

@author: ajay
"""
from FDwavePY.Sources.Source import Source

class Point(Source):
    def __init__(self):
        self.kind = 'Point'
        Source.__init__(self, name=None, 
                        freq=None, dt=0.001, T=1, t0=0, scale=1)