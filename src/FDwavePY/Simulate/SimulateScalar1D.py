#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:34:26 2024

@author: ajay
"""

from FDwavePY.Simulate.Derivative import Derivative
from FDwavePY.Simulate.BC import BC
import numpy as np


class SimulateScalar1D:
    def __init__(self):
        self.der = Derivative()
        self.bc = BC()
                

    def derive_prop(self):
        pass
    
    
    def check_stability(self, **kwargs):
        cflthreshold = kwargs.get('cflthreshold', 0.95)
        print('Check stability using courant condition.')
        cfl = self.mod.vp.mp.max()*self.src.dt/self.mod.vp.ax1.dh
        
        if cfl < cflthreshold:
            print(f'Courant condition satisfied, ({cfl} < Threshold {cflthreshold})')
        else:            
            raise ValueError(f'Courant condition is not satisfied, ({cfl} > Threshold {cflthreshold}).')
        
            
            
            
    
    def check_dispersion(self, fmax, MinPointsPerWavelength):
        print('Check dispersion conditions.')
        
        # find smallest wavelength
        lambda_min = self.mod.vp.mp.max()/fmax
        npts = lambda_min/self.mod.vp.ax1.dh
        
        if npts >= MinPointsPerWavelength: 
            print(f'Dispersion condition satisfied, ({npts} > Threshold {MinPointsPerWavelength})')
        else: 
            raise ValueError(f'Dispersion condition not satisfied, ({npts} < Threshold {MinPointsPerWavelength})')
            
    
    
    
    
    def add_point_source(self):
        pass 
        
    
    
    
    def simulate_ishot(self, ishot, **kwargs):
        vp = self.mod.vp
        dh = self.mod.vp.ax1.dh 
        dt = self.src.dt
        nt = self.src.nt
        fmax = self.src.freq        
        
        print(f'Simulation for: {self.mod.rheology}, {self.mod.dim}D')
        self.check_stability()        
        self.check_dispersion(fmax, 20) 
        
        
        ## select the derivative properties
        grid = kwargs.get('grid', 'collocated')
        order = kwargs.get('order', 2)
        accuracy = kwargs.get('accuracy', 2)        
        self.der.choose_derivative( grid, order, accuracy)
        
        
        ## Expand domain
        
        # Allocate new matrices
        p0 = np.zeros_like(self.mod.vp.mp)
        p1 = np.zeros_like(self.mod.vp.mp)
        p2 = np.zeros_like(self.mod.vp.mp)
        
        ## Find source receiver index locations 
        rloc = self.layout.rec[ishot].locx
        sloc = self.layout.src[ishot].locx       
            
        slocidx = self.mod.vp.ax1.get_index(sloc)
        rlocidx = self.mod.vp.ax1.get_index(rloc)
        print(slocidx)
        print(rlocidx)
        
        ## derived property 
        derprop = np.power(self.mod.vp.mp*dt/dh,2)
        
              
        ss = np.zeros((nt, p0.size))
        
        for i in range(nt):
            p1[slocidx] += self.src.svec[i]            
            p2 = 2*p1 - p0 + derprop * self.der.calc_derivative_1d(p1)
            
            # save snaps
            ss[i,:] = p2
            
            # change state
            p0=p1
            p1=p2
            
        return ss
        