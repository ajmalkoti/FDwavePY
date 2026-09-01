#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:43:48 2024

@author: ajay
"""
import numpy as np
import matplotlib.pyplot as plt
from FDwavePY.Models.Model import Model
from FDwavePY.Models.MaterialProperty import MaterialProperty1D


class Scalar1d(Model):
    """
    This module provides the Scalar medium  with vp only
    
    """
    def __init__(self, name):
        Model.__init__(self, name, 'scalar', 1)
        self.vp = MaterialProperty1D()
    
   
    #####################################################################    
    def homogeneous(self, vp, nodes, dh=1, x0=0):
        if isinstance(vp,(int, float)):
            self.name = 'homogeneous'
            self.vp.setter('vp', 'm/s', np.ones(nodes)*vp, dh=dh, x0=x0)
                
    
    def layered(self, vp, layer_thickness, dh=1):        
        raise NotImplementedError('Layered function not implemented yet')

    
    def random(self, vpmin, vpmax, nodes, dh=1, x0=0):
        self.name = 'Random'
        vec = vpmin + np.random.random(nodes)* (vpmax-vpmin)
        self.vp.setter('Vp', 'm/s', vec, dh=dh, x0=x0)

    def user(self, vp, dh, x0):
        self.vp.setter('Vp', 'm/s', vp, dh=dh, x0=x0)
        
    

    def plot(self, **kwargs):
        ylab= kwargs.get('ylab', 'Vp [m/s]')
        clr = kwargs.get('color', 'r')
        figsize = kwargs.get('figsize', (6,4))
        
        fig, ax = plt.subplots(1, 1, figsize=figsize)
        self.vp.plot(fig,ax,clr, ylab)
        plt.tight_layout()
        # raise NotImplementedError('Scaler model: plot function is not implemented')
        
        
        
        
        
if __name__ == "__main__":    
    m = Scalar1d('asdf')    
    m.homogeneous(2000, 100)    
    m.vp.plot()
    
    m.random(1200, 2000, 100)    
    m.vp.plot()
            
    m.plot()  