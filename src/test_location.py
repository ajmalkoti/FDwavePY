#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 23:48:08 2024

@author: ajay
"""

import FDwavePY as sim
import numpy as np 


s = sim.FDwavePY(rheo='sc', dim=1, skind='Point')    
s.mod.homogeneous(vp=1500, nodes=200, dh=2) 


vec = s.mod.vp.ax1.vec
N = len(vec)
s.layout.predef_snrn_fixed(sloc=[vec[N//2]], 
                           rloc=s.mod.vp.ax1.vec)

s.layout.plot()


print(s.layout.src[0].locx)
print(s.layout.rec[0].locx)
