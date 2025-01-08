#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 20:11:30 2024

@author: ajay
"""
import numpy as np 
import matplotlib.pyplot as plt
from FDwavePY.Layout.Layout1D import Layout1D
from FDwavePY.Layout.Layout2D import Layout2D
from FDwavePY.Layout.Layout3D import Layout3D      
        

class Layout:
    def __init__(self, **kwargs):
        
        dim = kwargs.get('dim', None)
        
        if not isinstance(dim, int):
            raise ValueError('The dimension must be provided.')
        if dim == 1:
            self.layout = Layout1D()
            
        elif dim == 2:
            self.layout = Layout2D()
            
        elif dim == 3:
            self.layout = Layout3D()
        
        else: 
            raise ValueError('Wrong number of dimensions.')


        