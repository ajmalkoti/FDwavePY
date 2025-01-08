#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:25:15 2024

@author: ajay
"""
import numpy as np 



class MaterialPropertyAxes:
    __slots__ = ('_name', '_unit', '_vec')
    def __init__(self):
        self.name = ''
        self.unit = ''
        self.vec = np.array([])
        
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, val):
        if isinstance(val, str):
            self._name = val
        else:
            raise ValueError('Axis name should be of string type.')
            
    @property
    def unit(self):
        return self._unit
    @unit.setter
    def unit(self, val):
        if isinstance(val, str):
            self._unit = val
        else:
            raise ValueError('Axis Unit should be of string type.')
        
    @property
    def vec(self):
        return self._vec
    
    @vec.setter 
    def vec(self, val):
        if isinstance(val, np.ndarray):
            self._vec = val
        else:
            raise ValueError('Axis vec should be of numpy array.')
        
            
            
    # #################################        
    # ####### Dependent properties
    # #################################
    @property
    def x0(self):
        return self.vec[0]
    

    @property
    def x1(self):
        return self.vec[-1]


    @property
    def dh(self):
        return self.vec[1]-self.vec[0]
    
    
    @property
    def nnodes(self):
        return self.vec.shape
    
    @property 
    def label(self):        
        return f'{self.name} [{self.unit}]'
    
    # ##############################
    # ###### Methods ################
    @classmethod
    def generate(cls, nodes, dh, x0, name, unit):        
        x = cls()
        x.name = name
        x.unit = unit
        x.vec = np.arange(nodes)*dh + x0

        return x
    
    
    def expand(self, begin=0, end=0):
        if begin>0:
            temp = np.flip(self.x0 -np.arange(1,begin+1)*self.dh )
            
            self.vec = np.hstack((temp, self.vec))
            
        if end>0:
            temp = self.x1 + np.arange(1,end+1)*self.dh 
            self.vec = np.hstack((self.vec, temp))
            
            
    def get_index(self, val):   
        if isinstance(val, (int, float)):            
            val = np.array(val)
        
        if isinstance(val, list):
            try:
                val = np.array(val)
            except Exception:
                raise ValueError('The value provided shoudl be int/float or a list/array of int/float.')
            
        if val.size == 1:
            idx = (np.abs(self.vec - val)).argmin()
        elif val.size > 1:
            idx = np.zeros(val.size)
            for i in range(val.size):
                idx[i] = (np.abs(self.vec - val[i])).argmin()
            
        # print(idx )
        return idx
        
        
        
        
# if __name__ == "__main__":
#     x = MaterialPropertyAxes()
#     x = MaterialPropertyAxes.generate(100, 5, 20, 'x', 'm/s')
#     print(x.nnodes)