#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:31:30 2024

@author: ajay
"""
from FDwavePY.Layout.Layout2D import Layout2D


class Layout3D(Layout2D): 
    def __init__(self, dim):
        self.slocz = None
        self.rlocz = None 