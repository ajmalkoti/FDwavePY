#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:31:24 2024

@author: ajay
"""
from FDwavePY.Layout.Layout1D import Layout1D


class Layout2D(Layout1D): 
    def __init__(self, dim):
        self.slocy = None
        self.rlocy = None        
        
