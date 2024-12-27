#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 14:43:15 2024

@author: ajay
"""

from FDwavePY.Simulate.Derivative import Derivative

class SimulateScalar3D(Derivative):
    def __init__(self):
        Derivative.__init__(self)
        
    
    def simulate(self, mod, src):        
        vp = mod.vp
        dh = mod.dh 
        dt = src.dt
        