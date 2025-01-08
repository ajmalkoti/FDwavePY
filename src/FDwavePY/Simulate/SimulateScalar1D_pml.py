#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:01:31 2025

@author: ajay
"""

class SimulateScalar1D_pml:
    def __init__(self):
        self.der = Derivative()
        self.bc = BC()
        self.ss = None
        self.dt = None        

    def derive_prop(self):
        pass
    
    
    def check_stability(self,  mod, src, **kwargs):
        cflthreshold = kwargs.get('cflthreshold', 0.95)
        print('Check stability using courant condition.')
        cfl = mod.vp.mp.max()*src.dt/mod.vp.ax1.dh
        
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
            
    
    
    
    def simulate_ishot(self,  ishot, mod, src, layout, **kwargs):
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
        rloc = layout.rec[ishot].locx
        sloc = layout.src[ishot].locx       
            
        slocidx = mod.vp.ax1.get_index(sloc)
        rlocidx = mod.vp.ax1.get_index(rloc)
        print(slocidx)
        print(rlocidx)
        
        ## derived property 
        derprop = np.power(mod.vp.mp*dt/dh,2)
        
              
        ss = np.zeros((nt, p0.size))
        
        for i in range(nt):
            if verbose == True:
                print(f'Iteration = {i}')
                
            p1[slocidx] += src.svec[i]            
            p2 = 2*p1 - p0 + derprop * self.der.calc_derivative_1d(p1)
            
            # save snaps
            ss[i,:] = p2
            
            # change state
            p0=p1
            p1=p2
            
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
    