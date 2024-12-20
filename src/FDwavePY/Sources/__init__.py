#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:53:19 2024

@author: ajay
"""

import numpy as np
import matplotlib.pyplot as plt
# from FDwavePY.Models.Point import Point
from FDwavePY.Source.Signature import Signature


from FDwavePY.Source.PointSource import PointSource
from FDwavePY.Source.LineSource import LineSource





class Sources: 
    def __init__(self, **kwargs):        
        kind = kwargs.get('kind', 'point')
        name = kwargs.get('name', 'Ricker')
    
        if kind in ['pt', 'point']:
            self.src = None
        
    
        
        

#     def plot(self, fig, ax):        
#         if fig is None or ax is None:
#             ax.plot()
            
        
    
        



# class Point(Source):
#     def __init__(self, name, kind, sig, dt, freq, scale, sx, sy=None, sz=None, order=None):
#         Source.__init__(self,name, kind, sig, dt, freq, scale, sx, sy=None, sz=None, order=None)


# class PointLine(Source):
#     def __init__(self, name, kind, sig, dt, freq, scale, sx, sy=None, sz=None, order=None):
#         Source.__init__(self,name, kind, sig, dt, freq, scale, sx, sy, sz, order)


# class MT(Source):
#     def __init__(self, name, kind, sig, dt, freq, scale):
#         Source.__init__(self,name, kind, sig, dt, freq, scale)


# class Sources:
#     def __init__(self, **kwargs):
#         name = kwargs.get('name', 'Ricker (default)')
#         rheo = kwargs.get('rheo', '')
#         dim = kwargs.get('dim', None)
        
#         if name.lower() in ['ricker', 'rk'] :
#                 self.src = Source(name)
                
                
                
                
                
                