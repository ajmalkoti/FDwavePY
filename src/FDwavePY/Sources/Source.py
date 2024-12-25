#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 11:20:32 2024

@author: ajay
"""
import numpy as np
import matplotlib.pyplot as plt

class Source:
    def __init__(self,**kwargs):
        self._kind = None
        self._name = None
        self._freq = None
        self._tvec = None
        self._svec = None
        self._scale= 1
        
        
    ##########################
    @property
    def kind(self):
        return self._kind
    
    @kind.setter
    def kind(self, val):
        if isinstance(val, str):
            self._kind = val
        else:
            raise ValueError('The source kind should be string type only.')
            
            
    ##########################
    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, val):
        if isinstance(val, str):
            self._name = val
        else: 
            raise ValueError('The source name should be string type only.')

    ##########################
    @property
    def tvec(self):
        if self._tvec is None: 
            raise ValueError('The source tvec not initialized yet.')
        else:
            return self._tvec
    
    @tvec.setter 
    def tvec(self, val):
        if isinstance(val, np.ndarray):
            if isinstance(val[0], (np.integer,np.floating)):
                self._tvec = val
                self._dt = np.diff(val)[0]
                self._t0 = val[0]
                self._T = val[-1]
        else: 
            raise ValueError('The source tvec should be a numpy array (inf/float) type only.')

    ##########################
    @property
    def dt(self):
        if self.tvec is None: 
            raise ValueError('For dt, first initialize the tvec')
        return self._dt    
    
    @property
    def T(self):
        if self.tvec is None: 
            raise ValueError('For T, first initialize the tvec')
        return self._T
    
    @property
    def t0(self):
        if self.tvec is None: 
            raise ValueError('For t0, first initialize the tvec')
        return self._t0
        
    @property
    def nt(self):        
        return self.svec.size
    
    ###########################################################
    @staticmethod 
    def sigsine(freq, dt, t0, T, scale):
        tvec = np.arange(0,T+dt, dt) - t0
        freq = np.array(freq)
        
        if freq.size ==1 : 
            sig = np.sin(2*np.pi*freq*tvec)
        else:
            sig = 0 
            for i in range(freq.size):            
                sig += np.sin(2*np.pi*freq[i]*tvec)
                
        return sig, tvec
    

    @staticmethod 
    def sigtriangle(freq, dt, t0, T, scale):
        Tp2 = 1/(2*freq)        
        
        N = int(Tp2//dt)
        
        tempvec = np.arange(0, N+1)*dt
        m = -1/(N*dt)
        
        yp = 1 + m*tempvec          # for positive time part
        yn = np.flip(yp)          # for negative time part
        
        y = np.concatenate((yn[0:-1], yp)) 
        
        tvec = np.arange(0,T+dt, dt)        
        sig = np.zeros_like(tvec)
        sig[0:2*N+1] = y       
        
        return sig, tvec
    
    @staticmethod
    def sigricker(freq, dt, t0, T, scale):
        tvec = np.arange(0,T+dt, dt)
        pft = np.pi*freq*(tvec-t0)
        pft2 = pft*pft
        sig = (1-2*pft2)*np.exp(-pft2)        
        return sig, tvec
    
    
    @staticmethod
    def siggaussian():
        pass
    
    
    @staticmethod
    def sigklauder():
        pass
    
    @staticmethod
    def sigormsby():
        pass

    # def update_param(self, **kwargs):

        

class Point(Source):
    def __init__(self):        
        Source.__init__(self)
        self.kind = 'Point'

    def userdefined(self, svec, tvec):
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
        
        
    def ricker(self, freq=20, dt=0.001, T=1, t0=.025, scale=1):
        self.name = 'Ricker'
        self.freq = freq        
        self.scale = scale        
        self.svec, self.tvec = self.sigricker(freq, dt, t0, T, scale)


    ##########################
    def plot(self, title=None, fig=None, ax=None, figsize=(4,2)):
        if fig is None or ax is None:
            fig, ax = plt.subplots(1,1,figsize=figsize)
        
        ax.plot(self.tvec, self.svec)
        ax.set_xlabel('Time')
        ax.set_ylabel('Amplitude')
        
        t = title if title else self.name
        ax.set_title(t)
        plt.tight_layout()
        
        
        
        
        

class MomentTensor(Source):
    def __init__(self):
        self.kind = 'MomentTensor'
        # Source.__init__(self, name=None, 
        #                 freq=None, dt=0.001, T=1, t0=0, scale=1)
        
        raise NotImplementedError('MT type source not implemented yet.')




