#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:54:08 2024

@author: ajay
"""
import numpy as np
import matplotlib.pyplot as plt
from FDwavePY.Models.Scalar1d import Scalar1d


class Acoustic1d(Scalar1d):
    def __init__(self, name):
        Scalar1d.__init__(self, name)
        self._rho = None
    
    ###################
    @property 
    def rho(self):
        return self._rho
    
    @rho.setter 
    def rho(self, val):
        if isinstance(val, np.ndarray):
            if val.ndim ==1 :
                self._rho = val
    
    
    ##################################################
    ##################################################
    
    def homogeneous(self, vp, rho, nodes, dh=1, x0=0):
        if isinstance(vp,(int, float)):
            self.vp = np.ones(nodes)*vp
            
        if isinstance(rho, (int, float)):
            self.rho = np.ones(nodes)*rho
            
        self.nodes = nodes
        self.default_xvec(dh, x0)
            
        
        
    
    def layered(self, vp, layer_thickness, dh=1):
        
        pass
    
    def random(self, **kwargs):
        pass
    
    
    def plot(self, **kwargs):
        lab= kwargs.get('lab', ['Vp', 'Rho'])
        clr = kwargs.get('color', ['r','b'])
        overlay = kwargs.get('overlay', True)
        
        if overlay == True:
            fig, ax = plt.subplots(1,1)
            self.vecplot(self.xvec, self.vp, fig=fig, ax=ax, label=lab[0], color= clr[0])
            self.vecplot(self.xvec, self.rho, fig=fig, ax=ax, label=lab[1], color= clr[1])
            
        else: 
            fig, ax = plt.subplots(2,1)
            self.vecplot(self.xvec, self.vp, fig=fig, ax=ax[0], label=lab[0], color=clr[0])
            self.vecplot(self.xvec, self.rho, fig=fig, ax=ax[1], label=lab[1], color=clr[1])
            
        plt.legend()
        # plt.show()
        # raise NotImplementedError('Acoustic model: plot function is not implemented')