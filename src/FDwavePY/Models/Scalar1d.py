#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:43:48 2024

@author: ajay
"""
import numpy as np
from FDwavePY.Models.Model1d import Model1d

class Scalar1d(Model1d):
    def __init__(self, name):
        Model1d.__init__(self, name, 'acoustic', 1)
        self._vp = None
    
    ###################
    @property 
    def vp(self):
        return self._vp
    
    @vp.setter 
    def vp(self, val):
        if isinstance(val, np.ndarray):
            if val.ndim ==1 :
                self._vp = val
        else:
            raise ValueError('The vp array should be a numpy array.')

   
    #####################################################################
    #####################################################################
    def homogeneous(self, vp, nodes, dh=1, x0=0):
        if isinstance(vp,(int, float)):
            self.vp = np.ones(nodes)*vp        
        
        self.nodes = nodes
        self.default_xvec(dh, x0)
        
    
    def layered(self, vp, layer_thickness, dh=1):        
        pass
    
    def random(self, **kwargs):
        pass
    

    def plot(self):
        self.vecplot(self.xvec, self.vp, fig=None, ax=None)
        # raise NotImplementedError('Scaler model: plot function is not implemented')