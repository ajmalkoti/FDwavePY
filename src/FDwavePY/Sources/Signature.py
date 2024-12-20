#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 17:26:09 2024

@author: ajay
"""
import numpy as np
import matplotlib.pyplot as plt


class Signature:
    def __init__(self, name=None, freq=None, dt=0.001, T=1, t0=0, scale=1, sig=None,**kwargs):
        self.name = name
        self.dt = dt
        self.T = T
        self.t0 =t0
        self.freq = freq
        self.scale= scale
        self.sig = sig
        
    @staticmethod
    def ricker(freq, dt, t0, T, scale):
        tvec = np.linspace(0,T, dt) + t0
        pft = np.pi*freq*(tvec-t0)
        pft2 = pft*pft
        sig = (1-2*pft2)*np.exp(-pft2)        
        return sig, tvec

    @staticmethod
    def gaussian():
        pass
    
    @staticmethod
    def klauder():
        pass
    
    @staticmethod
    def ormsby():
        pass