#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 14:42:53 2024

@author: ajay
"""

from FDwavePY.Simulate.Derivative import Derivative
from FDwavePY.Simulate.BC import BC
import numpy as np
import matplotlib.pyplot as plt



class SimulateScalar2D(Derivative):
    def __init__(self):
        self.der = Derivative()
        self.bc = BC()
        self.ss = None
        self.dt = None
        
    def derive_prop(self):
        pass
    
    
    def check_stability(self, mod, src, **kwargs):
        cflthreshold = kwargs.get('cflthreshold', 0.95)
        print('Check stability using courant condition.')
        cfl = mod.vp.mp.max()*src.dt/(mod.vp.ax1.dh* np.sqrt(mod.vp.mp.ndim))
        
        if cfl < cflthreshold:
            print(f'Courant condition satisfied, ({cfl} < Threshold {cflthreshold})')
        else:            
            raise ValueError(f'Courant condition is not satisfied, ({cfl} > Threshold {cflthreshold}).')
            
            
            
    def check_dispersion(self, mod, src, fmax, MinPointsPerWavelength):
        print('Check dispersion conditions.')
        
        # find smallest wavelength
        lambda_min = mod.vp.mp.max()/fmax
        npts = lambda_min/mod.vp.ax1.dh
        
        if npts >= MinPointsPerWavelength: 
            print(f'Dispersion condition satisfied, ({npts} > Threshold {MinPointsPerWavelength})')
        else: 
            raise ValueError(f'Dispersion condition not satisfied, ({npts} < Threshold {MinPointsPerWavelength})')
            
    
    
    def simulate_ishot(self, ishot, mod, src, layout, **kwargs):
        vp = mod.vp
        dh = mod.vp.ax1.dh 
        dt = src.dt
        nt = src.nt
        fmax = src.freq        
        
        verbose = kwargs.get('verbose', False)
        
        print(f'Simulation for: {mod.rheology}, {mod.dim}D')
        self.check_stability(mod, src)
        self.check_dispersion(mod,src, fmax, 20) 
        
        
        ## select the derivative properties
        grid = kwargs.get('grid', 'collocated')
        order = kwargs.get('order', 2)
        accuracy = kwargs.get('accuracy', 2)        
        self.der.choose_derivative( grid, order, accuracy)
        
        
        ## Expand domain
        
        # Allocate new matrices
        p0 = np.zeros_like(mod.vp.mp)
        p1 = np.zeros_like(mod.vp.mp)
        p2 = np.zeros_like(mod.vp.mp)
        
        ## Find source receiver index locations 
        rlocx = layout.rec[ishot].locx
        rlocz = layout.rec[ishot].locz
        
        slocx = layout.src[ishot].locx       
        slocz = layout.src[ishot].locz
        
        slocidx = mod.vp.ax1.get_index(slocx).astype(int)
        slocidz = mod.vp.ax2.get_index(slocz).astype(int)
        
        rlocidx = mod.vp.ax1.get_index(rlocx).astype(int)
        rlocidz = mod.vp.ax2.get_index(rlocz).astype(int)
        
        print(slocidx)
        print(rlocidx)
        
        ## derived property 
        derprop = np.power(mod.vp.mp*dt/dh,2)
        
              
        ss = np.zeros((nt, p0.shape[1]))
        
        for i in range(nt):
            if verbose == True:
                print(f'Iteration = {i}')
            p1[slocidz, slocidx] += src.svec[i]            
            derx= self.der.calc_derivative(p1, axis='x')
            derz = self.der.calc_derivative(p1, axis='z')
            
            p2 = 2*p1 - p0 + derprop * (derx + derz)
            
            # save snaps
            ss[i,rlocidx] = p2[rlocidz,rlocidx]
            
            # change state
            p0 = p1
            p1 = p2
            
        ######### 
        ## Save variable for future use.
        self.ss = ss
        self.dt = dt 
        
    def plot_receiver_response(self, figsize=[8,5],**kwargs):
        
        fig, ax = plt.subplots(1,1, figsize= figsize)        
        extent = [1,self.ss.shape[1], self.ss.shape[0]*self.dt, 0]        
        ax.imshow(self.ss,extent=extent, aspect='auto')
        ax.set_xlabel('Receiver Number')
        ax.set_ylabel('Time[s]')
        
        