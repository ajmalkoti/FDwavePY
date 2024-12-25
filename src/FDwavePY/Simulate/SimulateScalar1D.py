#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:34:26 2024

@author: ajay
"""

from FDwavePY.Simulate.Derivative import Derivative
from FDwavePY.Simulate.BC import BC
import numpy as np


class SimulateScalar1D:
    def __init__(self):
        self.der = Derivative()
        self.bc = BC()
                

    def derive_prop(self):
        pass
    
    
    def check_stability(self):
        print('Check stability')
        

    
    def check_dispersion(self):
        print('Check dispersion')
    
    
    def add_point_source(self):
        pass 
    
    
    
    def simulate(self):
        vp = self.mod.vp
        dh = self.mod.dh 
        dt = self.src.dt
        nt = self.src.nt
        
        for i in range(nt):
            self.add_point_source(i)        
            self.der.calc_derivative_1d(vp)
            
        
        
        
    
            
    # def correct_src_rec_loc(self,):
        