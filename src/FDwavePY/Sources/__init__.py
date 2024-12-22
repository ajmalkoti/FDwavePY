#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:53:19 2024

@author: ajay
"""

import numpy as np
import matplotlib.pyplot as plt
from FDwavePY.Sources.Source import Point
from FDwavePY.Sources.Source import MomentTensor



class Sources: 
    def __init__(self, **kwargs):        
        skind = kwargs.get('skind', 'point')
        if isinstance(skind, str):
            skind = skind.lower()
            
        # name = kwargs.get('name', 'Ricker')
    
        if skind in ['p', 'point']:
            self.src = Point()
        
        elif skind in ['mt', 'momenttensor']:
            self.src = MomentTensor()
        else:
            raise ValueError('Permitted values for Stype are= [p, point, mt, momenttnsor].')
        
        

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
                
                
                
                
                
                