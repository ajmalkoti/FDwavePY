#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:21:09 2024

@author: ajay
"""
import numpy as np 

class axis:
    @property
    def vec(self):
        return self._vec
    
    @vec.setter 
    def vec(self, val):
        if isinstance(val, np.ndarray):
            self._xvec = val
            
    ####### Dependent properties
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
    
    
    ###### Methods 
    def ax_generate(self, nodes, dh, x0):
        self.vec = np.arange(nodes)*dh + x0
    
    
    def ax_expand(self, begin=0, end=0):
        if begin>0:
            temp = self.x0 -np.arange(1,begin+1)*self.dh 
            self.vec = np.hstack((temp, self.vec))
        if end>0:
            temp = self.x1 + np.arange(1,begin+1)*self.dh 
            self.vec = np.hstack((self.vec, temp))
            


class material_prop_1d:
    def __init__(self, name, val):
        self.name = name
        self.val = val
        
    def mp_expand(self, begin=0, end=0):         
        if self.val is None:
            raise ValueError('Material property not assigned value')
            
        if begin>0:                
            out = np.hstack((np.ones(begin)*self.val[0], self.val))
            
        if end>0:
            out = np.hstack((self.val, self.val[-1]*np.ones(end)))
            
            
        
        

################################
class Model:
    """ Model class contains basic attributes and methods that are common 
    to all models 1d/2d/3d models.
    """
    def __init__(self, name, rheology, dim):
        self.name = name        
        self.rheology = rheology
        self.dim = dim
        
        self.xaxis = axis()        
    

    def __str__(self):
        title =[f'Model description:',
                f'Name : {self.name}',
                f'Rheolgy :{self.rheology} ({self.dim}D)',
                ]
        ''.join(title, '\n')
        
    
    @property
    def name(self):
        return self._name

    @name.setter 
    def name(self, val):
        if isinstance(val, str):
            self._name = val
        else:
            raise ValueError('The name should be of string type')
        
    ################
    @property
    def rheo(self):
        return self._rheo
    @rheo.setter 
    def rheo(self, val):
        if isinstance(val, str):
            self._rheo = val
        else:
            raise ValueError('The model rheo should be of string type.')
            
            
    ################
    @property
    def dim(self):
        return self._dim
    
    @dim.setter 
    def dim(self, val):
        if val in [1,2,3]:
            self._dim = val
        else:
            raise ValueError('The model dim should be of int type (=1/2/3).')
            

