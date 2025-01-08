#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:25:45 2024

@author: ajay
"""


import numpy as np
import matplotlib.pyplot as plt
from FDwavePY.Sources.Source import Source


class Point(Source):
    def __init__(self):        
        Source.__init__(self)
        self.kind = 'Point'
        
    @property
    def nt(self):
        return self.tvec.size
    
    @property 
    def t0(self):
        return self.tvec[0]
    

    def userdefined(self, svec, tvec):
        self.name = 'userdefined'
        self.svec = svec
        self.tvec = tvec

    def sine(self, freq=20, dt=0.001, T=1, t0=.025, scale=1):
        self.name = 'Sine'
        self.freq = freq        
        self.scale = scale        
        self.svec, self.tvec = self.sigsine(freq, dt, t0, T, scale)
        
    def triangle(self, freq=20, dt=0.001, T=1, t0=.025, scale=1):
        self.name = 'Triangle'
        self.freq = freq 
        self.scale = scale
        self.svec, self.tvec = self.sigtriangle(freq, dt, t0, T, scale)
        
        
    def ricker(self, freq=20, dt=0.001, T=1, t0=.05, scale=1):
        self.name = 'Ricker'
        self.freq = freq        
        self.scale = scale        
        self.svec, self.tvec = self.sigricker(freq, dt, t0, T, scale)


    ##########################
    def plot(self, title=None, fig=None, ax=None, figsize=(4,2), xlim=None):
        if fig is None or ax is None:
            fig, ax = plt.subplots(1,1,figsize=figsize)
        
        ax.plot(self.tvec, self.svec)
        ax.set_xlabel('Time')
        ax.set_ylabel('Amplitude')
        
        t = title if title else self.name
        ax.set_title(t)
        if xlim is not None:
            ax.set_xlim(xlim)
    
        ax.grid()
        plt.tight_layout()