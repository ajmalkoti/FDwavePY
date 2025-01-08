#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:17:24 2024

@author: ajay
"""

from  FDwavePY.Models import Models
from  FDwavePY.Sources import Sources
from FDwavePY.Layout import Layout
from FDwavePY.Simulate import Simulate



class FDwavePY(Simulate):
    
    def __init__(self,**kwargs):
        self.verbose = True
        Models.__init__(self,**kwargs)
        Sources.__init__(self,**kwargs)                
        
        Layout.__init__(self, **kwargs)        
        Simulate.__init__(self, **kwargs)
        
        
    def simulate_ishot(self, shotno):
        return self.sim.simulate_ishot(shotno, self.mod, self.src, self.layout, \
                                       verbose=self.verbose)
        