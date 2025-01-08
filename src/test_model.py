#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:13:48 2024

@author: ajay
"""
import FDwavePY as sim
import numpy as np 

#####################################
##### for 1D Scalar
s = sim.FDwavePY(rheo='sc', dim=1, skind='Point')    
s.mod.homogeneous(vp=2000, nodes=200, dh=1)   
s.mod.plot()

## Access model class
print(s.mod.name)
print(s.mod.rheology)
print(s.mod.dim)


## Acess material properties
print('Vp Name', s.mod.vp.name)
print('Vp Unit', s.mod.vp.unit)
print('Vp-Material Property ', s.mod.vp.mp)

## Acess material properties
print(s.mod.vp.ax1.name)
print(s.mod.vp.ax1.unit)
print(s.mod.vp.ax1.vec)

## dependent properties
print(s.mod.vp.ax1.x0)
print(s.mod.vp.ax1.x1)
print(s.mod.vp.ax1.nnodes)
print(s.mod.vp.ax1.dh)




#####################################
##### for 1D Acoustic
s = sim.FDwavePY(rheo='ac', dim=1, skind='Point')    
s.mod.homogeneous(vp=2000, rho= 1000, nodes=200, dh=1)   
s.mod.plot()


#####################################
# for 2D Scalar
s = sim.FDwavePY(rheo='sc', dim=2, skind='Point')    
s.mod.homogeneous(vp=2000, nodes=(100,200), dh=1)   
s.mod.plot()



#####################################
# for 2D Acoustic
s = sim.FDwavePY(rheo='ac', dim=2, skind='Point')    
s.mod.homogeneous(vp=2000, rho=1000, nodes=(100,200), dh=1)   
s.mod.plot()



