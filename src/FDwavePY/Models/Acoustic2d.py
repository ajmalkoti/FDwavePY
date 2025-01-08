#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 02:24:40 2024

@author: ajay
"""

import numpy as np
import matplotlib.pyplot as plt
from FDwavePY.Models.Model import Model
from FDwavePY.Models.MaterialProperty import MaterialProperty2D


class Acoustic2d(Model):
    def __init__(self, name):
        Model.__init__(self, name, 'acoustic', 2)
        self.vp = MaterialProperty2D()
        self.rho = MaterialProperty2D()
    
   
    #####################################################################    
    def homogeneous(self, vp, rho, nodes, dh=1, x0=0):
        if isinstance(vp,(int, float)):
            self.name = 'homogeneous'
            self.vp.setter('vp', 'm/s', np.ones(nodes)*vp, dh=dh, x0=x0)
            self.rho.setter('Density', 'g/cc', np.ones(nodes)*rho, dh=dh, x0=x0)
                
    
    def layered(self, vp, rho, layer_thickness, dh=1):        
        raise NotImplementedError('Layered function not implemented yet')

    
    def random(self, vprange, rhorange, nodes, dh=1, x0=0):
        self.name = 'Random'
        vec = vprange[0] + np.random.random(nodes)* (vprange[1]-vprange[0])
        self.vp.setter('Vp', 'm/s', vec, dh=dh, x0=x0)
        
        vec = rhorange[0] + np.random.random(nodes)* (rhorange[1]- rhorange[0])
        self.rho.setter('Rho', 'g/cc', vec, dh=dh, x0=x0)
        

    def user(self, vp, rho, dh, x0):
        self.vp.setter('Vp', 'm/s', vp, dh=dh, x0=x0)
        self.rho.setter('Density', 'g/cc', rho, dh=dh, x0=x0)
    

    def plot(self, **kwargs):
        ylab= kwargs.get('ylab', 'Vp [m/s]')
        cmap = kwargs.get('cmap', 'viridis')
        figsize = kwargs.get('figsize', (6,4))
        
        fig, ax = plt.subplots(1, 2, figsize=figsize)
        
        self.vp.plot(fig,ax[0], cmap=cmap)
        self.rho.plot(fig,ax[1], cmap=cmap)
        plt.tight_layout()
        
        # raise NotImplementedError('Scaler model: plot function is not implemented')
        
        
        
        
        
# if __name__ == "__main__":
    
# m = Scalar2d('asdf')    
# m.homogeneous(2000, (50, 100))
# m.vp.plot()

# m.random(1200, 2000, (50, 100))    
# m.vp.plot()
        