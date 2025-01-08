#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 22:21:12 2024

@author: ajay
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:21:09 2024

@author: ajay
"""
import numpy as np 
    

class Model:
    """ Model class contains basic attributes and methods that are common 
    to all models 1d/2d/3d models.
    """
    def __init__(self, name, rheology, dim):
        self.name = name        
        self.rheology = rheology
        self.dim = dim
        
         
    

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