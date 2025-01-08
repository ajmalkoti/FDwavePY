#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:27:23 2024

@author: ajay
"""



# import numpy as np
# import matplotlib.pyplot as plt
# from FDwavePY.Sources.Source import Point
# from FDwavePY.Sources.Source import MomentTensor

from FDwavePY.Simulate.SimulateScalar1D import SimulateScalar1D
from FDwavePY.Simulate.SimulateScalar2D import SimulateScalar2D


class Simulate:
    
    def __init__(self, **kwargs):
        rheo = kwargs.get('rheo', None)
        dim = kwargs.get('dim', None)

        if rheo in ['sc', 'scalar']:
            if dim ==1:
                # self.sim = SimulateScalar1D()
                self.sim = SimulateScalar1D()
                
            elif dim == 2:
                self.sim = SimulateScalar2D()
                
            elif dim == 3:
                self.sim = None
            
        elif rheo in ['ac', 'acoustic']:
            if dim ==1:
                self.sim = None
                
            elif dim == 2:
                self.sim = None
                
            elif dim == 3:
                self.sim = None
        