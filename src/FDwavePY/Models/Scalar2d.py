#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 01:27:35 2024

@author: ajay
"""

import numpy as np
import matplotlib.pyplot as plt
from FDwavePY.Models.Model import Model
from FDwavePY.Models.MaterialProperty import MaterialProperty2D


class Scalar2d(Model):
    def __init__(self, name):
        Model.__init__(self, name, 'scalar', 2)
        self.vp = MaterialProperty2D()
    
   
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
        cmap = kwargs.get('cmap', 'viridis')
        figsize = kwargs.get('figsize', (6,4))
        
        fig, ax = plt.subplots(1, 1, figsize=figsize)
        
        self.vp.plot(fig,ax, cmap=cmap)
        plt.tight_layout()
        # raise NotImplementedError('Scaler model: plot function is not implemented')
        
        
        
        
        
# if __name__ == "__main__":
    
# m = Scalar2d('asdf')    
# m.homogeneous(2000, (50, 100))
# m.vp.plot()

# m.random(1200, 2000, (50, 100))    
# m.vp.plot()
        