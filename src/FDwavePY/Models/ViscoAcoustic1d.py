#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:19:26 2024

@author: ajay
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:54:08 2024

@author: ajay
"""
import numpy as np
import matplotlib.pyplot as plt
from FDwavePY.Models.Acoustic1d import Acoustic1d


class ViscoAcoustic1d(Acoustic1d):
    def __init__(self, name):
        Acoustic1d.__init__(self, name)
        self._rho = None
    
    ###################
    @property 
    def qp(self):
        return self._qp
    
    @qp.setter 
    def qp(self, val):
        if isinstance(val, np.ndarray):
            if val.ndim ==1 :
                self._qp = val
    
    
    ##################################################
    ##################################################
    
    def homogeneous(self, vp, rho, qp, nodes, dh=1, x0=0):
        if isinstance(vp,(int, float)):
            self.vp = np.ones(nodes)*vp
            
        if isinstance(rho, (int, float)):
            self.rho = np.ones(nodes)*rho
        
        if isinstance(qp, (int, float)):
            self.qp = np.ones(nodes)*qp
            
        self.nodes = nodes
        self.default_xvec(dh, x0)


    def layered(self, vp, layer_thickness, dh=1):        
        pass
    
    def random(self, **kwargs):
        pass
    
    def user(self, **kwargs):
        pass
    
    
    def plot(self, **kwargs):
        ylab= kwargs.get('ylab', ['Vp [m/s]', 'Rho [kg/m3]','Qp'])
        clr = kwargs.get('color', ['r','b', 'g'])
        overlay = kwargs.get('overlay', True)
        figsize = kwargs.get('figsize', (6,4))
        
        if overlay == True:
            fig, ax = plt.subplots(1, 1, figsize=figsize)
            self.vecplot(self.xvec, self.vp, fig=fig, ax=ax, label=ylab[0], color= clr[0])
            self.vecplot(self.xvec, self.rho, fig=fig, ax=ax, label=ylab[1], color= clr[1])
            self.vecplot(self.xvec, self.qp, fig=fig, ax=ax, label=ylab[2], color= clr[2])
            plt.legend()
            
        else: 
            fig, ax = plt.subplots(3, 1, figsize=figsize)
            self.vecplot(self.xvec, self.vp, fig=fig, ax=ax[0], color=clr[0], ylab=ylab[0])
            self.vecplot(self.xvec, self.rho, fig=fig, ax=ax[1], color=clr[1], ylab=ylab[1])
            self.vecplot(self.xvec, self.qp, fig=fig, ax=ax[2], color=clr[2], ylab=ylab[2])
            plt.tight_layout()
        # 
        # plt.show()
        # raise NotImplementedError('Acoustic model: plot function is not implemented')