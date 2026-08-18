#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:28:22 2024

@author: ajay
"""

import numpy as np
import matplotlib.pyplot as plt
from FDwavePY.Models.Elastic1d import Elastic1d


class ViscoElastic1d(Elastic1d):
    def __init__(self, name):
        Elastic1d.__init__(self, name)
        self._vs = None
    
    ###################
    @property 
    def qp(self):
        return self._qp
    
    @qp.setter 
    def qp(self, val):
        if isinstance(val, np.ndarray):
            if val.ndim ==1 :
                self._qp = val
                
    ###################
    @property 
    def qs(self):
        return self._qs
     
    @qs.setter 
    def qs(self, val):
        if isinstance(val, np.ndarray):
            if val.ndim ==1 :
                self._qs = val
    
    
    ##################################################    
    def homogeneous(self, vp, vs, rho, qp, qs, nodes, dh=1, x0=0):
        if isinstance(vp,(int, float)):
            self.vp = np.ones(nodes)*vp
        
        if isinstance(vs,(int, float)):
            self.vs = np.ones(nodes)*vs
            
        if isinstance(rho, (int, float)):
            self.rho = np.ones(nodes)*rho
            
        if isinstance(qp, (int, float)):
            self.qp = np.ones(nodes)*qp
            
        if isinstance(qp, (int, float)):
            self.qs = np.ones(nodes)*qs
            
        self.nodes = nodes
        self.default_xvec(dh, x0)
            
    
    def layered(self, vp, layer_thickness, dh=1):
        pass
    
    def random(self, **kwargs):
        pass
    
    def user(self, **kwargs):
        pass
    
    
    def plot(self, **kwargs):
        ylab= kwargs.get('ylab', ['Vp [m/s]', 'Vp [m/s]', 'Rho [kg/m3]', 'Qp', 'Qs'])
        clr = kwargs.get('color', ['r', 'g', 'b', 'k', 'm'])
        overlay = kwargs.get('overlay', True)
        figsize = kwargs.get('figsize', (6,10))
        
        if overlay == True:
            fig, ax = plt.subplots(1,1, figsize=figsize)
            self.vecplot(self.xvec, self.vp, fig=fig, ax=ax, label=ylab[0], color= clr[0])
            self.vecplot(self.xvec, self.vs, fig=fig, ax=ax, label=ylab[1], color= clr[1])
            self.vecplot(self.xvec, self.rho, fig=fig, ax=ax, label=ylab[2], color= clr[2])
            self.vecplot(self.xvec, self.qp, fig=fig, ax=ax, label=ylab[3], color= clr[3])
            self.vecplot(self.xvec, self.qs, fig=fig, ax=ax, label=ylab[4], color= clr[4])
            plt.legend()
            
        else: 
            fig, ax = plt.subplots(5,1, figsize=figsize)
            self.vecplot(self.xvec, self.vp, fig=fig, ax=ax[0], color=clr[0], ylab=ylab[0])
            self.vecplot(self.xvec, self.vs, fig=fig, ax=ax[1], color=clr[1], ylab=ylab[1])
            self.vecplot(self.xvec, self.rho, fig=fig, ax=ax[2], color=clr[2], ylab=ylab[2])
            
            self.vecplot(self.xvec, self.qp, fig=fig, ax=ax[3], color=clr[3], ylab=ylab[3])
            self.vecplot(self.xvec, self.qs, fig=fig, ax=ax[4], color=clr[4], ylab=ylab[4])
            plt.tight_layout()
            
            
            