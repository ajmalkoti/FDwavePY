#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:23:08 2024

@author: ajay
"""
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

from FDwavePY.Models.MaterialPropertyAxes import MaterialPropertyAxes 

class MaterialProperty1D:
    def __init__(self):
        self._name = None
        self._unit = None
        self._mp = None        
        self.ax1 = MaterialPropertyAxes()
        
    @property 
    def name(self):
        return self._name
    @name.setter 
    def name(self, val):
        if isinstance(val, str):
            self._name = val 
            
    @property 
    def unit(self):
        return self._unit
    @unit.setter 
    def unit(self,  val):
        if isinstance(val, str):
            self._unit = val
           
    
    
    @property 
    def mp(self):
        return self._mp
    @mp.setter 
    def mp(self,  val):
        if not isinstance(val, np.ndarray):
            raise ValueError('The assigned property should be a numpy array (1D).')
            
        if not(val.ndim == 1):
            raise ValueError('The assigned property should be a 1D array')

        self._mp = val
            
            
    
    @property
    def label(self):
        return f'{self.name} [{self.unit}]'
    
    
    #################
    ### METHODS
    #################
    def setter(self, name, unit, mp, dh=5, x0=0):
        self.name = name
        self.mp = mp
        self.unit = unit
        nodes = mp.size
        self.ax1 = MaterialPropertyAxes.generate(nodes, dh, x0, 'x', 'm')
        
    
    def expand(self, begin=0, end=0):         
        if self.mp is None:
            raise ValueError('Material property not assigned value')            
        
        if begin>0:                
            self.mp = np.hstack((np.ones(begin)* self.mp[0], self.mp))
        if end>0:
            self.mp = np.hstack((self.mp, self.mp[-1]*np.ones(end)))        
        
        self.ax1.expand(begin=begin, end= end)
        
            
    def plot(self, fig= None, ax=None, color='b', label=''):
        if fig is None or ax is None:
            fig, ax = plt.subplots(1,1)
            
        ax.plot(self.ax1.vec, self.mp, c=color, label=label)
        lab = self.ax1.name
        ax.set_xlabel(self.ax1.label)
        ax.set_ylabel(self.label)
        
        
            
    
#############################################
#############  2D 
#############################################
        
class MaterialProperty2D(MaterialProperty1D):
    def __init__(self):
        MaterialProperty1D.__init__(self)
        self.ax2 = MaterialPropertyAxes()
     
    @property 
    def mp(self):
        return self._mp
    @mp.setter 
    def mp(self,  val):
        if not isinstance(val, np.ndarray):
            raise ValueError('The assigned property should be a numpy array (1D).')
            
        if not (val.ndim == 2):
            raise ValueError('The assigned property should be a 2D array')

        self._mp = val
        
    #################
    ### METHODS
    #################
    def setter(self, name, unit, mp, dh=5, x0=0):
        self.name = name
        self.mp = mp
        self.unit = unit
        nodes = mp.shape
        self.ax1 = MaterialPropertyAxes.generate(nodes[1], dh, x0, 'x', 'm')
        self.ax2 = MaterialPropertyAxes.generate(nodes[0], dh, x0, 'z', 'm')
        
        
    def expand(self, left=0, right=0, top=0, bottom=0):
        if self.mp is None:
            raise ValueError('Material property not assigned value')            
        
        raise ValueError('Not yet implemented')
        # if left>0:                
        #     self.mp = np.hstack((np.ones(begin)* self.mp[0], self.mp))
        # if right>0:
        #     self.mp = np.hstack((self.mp, self.mp[-1]*np.ones(end)))        
        
        # self.ax1.expand(begin=begin, end= end)
        
            
    def plot(self, fig= None, ax=None, cmap='viridis'):
        if fig is None or ax is None:
            fig, ax = plt.subplots(1,1)
            
        h = ax.imshow(self.mp, cmap=cmap)
        # fig.colorbar(h, ax=ax, shrink=.6, pad=0.05)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)           
        plt.colorbar(h, cax=cax)
        
        ax.set_xlabel(self.ax1.label)
        ax.set_ylabel(self.ax2.label)    
        
        
            
            

#############################################
#############  3D 
#############################################        
class MaterialProperty3D:
    def __init__(self, name, val):
        self.name = name
        self.mp = val
        self.ax1 = MaterialPropertyAxes()
        self.ax2 = MaterialPropertyAxes()
        self.ax3 = MaterialPropertyAxes()
        
    def mp_expand(self, begin=0, end=0):         
        if self.mp is None:
            raise ValueError('Material property not assigned value')
            
        if begin>0:                
            out = np.hstack((np.ones(begin)*self.mp[0], self.mp))
            
        if end>0:
            out = np.hstack((self.mp, self.mp[-1]*np.ones(end)))
            
            


# if __name__ == "__main__":         
#     x = MaterialProperty1D()
#     x.setter('vp', 'm/s', np.arange(100), dh=5, x0=50)
#     x.plot()
    
#     x.expand(begin=5, end=10)
#     x.plot()
#     print(x.mp.size)


# x = MaterialProperty2D()
# vp = np.tile(np.arange(100), (50,1))
# x.setter('vp', 'm/s', vp, dh=5, x0=50)
# x.plot()