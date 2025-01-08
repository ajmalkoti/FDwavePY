#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:53:19 2024

@author: ajay
"""

# import numpy as np
# import matplotlib.pyplot as plt
from FDwavePY.Sources.Point import Point
from FDwavePY.Sources.MomentTensor import MomentTensor



class Sources: 
    def __init__(self, **kwargs):        
        skind = kwargs.get('skind', 'point')
        if isinstance(skind, str):
            skind = skind.lower()
            
        
    
        if skind in ['p', 'point']:
            self.src = Point()
        
        elif skind in ['mt', 'momenttensor']:
            self.src = MomentTensor()
        else:
            raise ValueError('Permitted values for Stype are= [p, point, mt, momenttnsor].')
        
        

                
                
                
                
                