#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:07:06 2024

@author: ajay
"""
import numpy as np
import matplotlib.pyplot as plt
from FDwavePY.Models.Model import Model


class Model1d(Model):
    def __init__(self, name, rheology, dim, dh=None, xvec=None):
        Model.__init__(self, name, rheology=rheology, dim=dim)
     
    
    ###################
    def default_xvec(self, dh, x0):
        self.xvec = np.arange(self.nodes)*dh + x0
        
        
    def vecplot(self, xvec, yvec, fig=None, ax=None, color='b', label='', ylab='', xlab='x [m]'):
        if fig is None or ax is None:
            fig, ax = plt.subplots(1,1)
            
        ax.plot(xvec, yvec, c=color, label=label)
        ax.set_xlabel(xlab)
        ax.set_ylabel(ylab)
       

