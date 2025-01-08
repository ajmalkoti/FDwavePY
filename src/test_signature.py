#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 23:33:54 2024

@author: ajay
"""

import FDwavePY as sim
import numpy as np 





#################################################
############ TEST signature #####################
s = sim.FDwavePY(rheo='sc', dim=1, skind='Point')    
s.mod.homogeneous(vp=1500, nodes=200, dh=2)   

s.src.ricker(freq=20, dt=0.001, T=1, t0=.05, scale=1)
s.src.plot(xlim = [0,.2])


print(s.src.name)
print(s.src.freq)
print(s.src.scale)
print(s.src.dt)

print(s.src.tvec)
print(s.src.svec)




s.src.sine(freq=20, dt=0.001, T=1, t0=.025, scale=1)
s.src.plot(xlim = [0,.2])