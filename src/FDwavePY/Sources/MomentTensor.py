#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 16:27:48 2024

@author: ajay
"""

import numpy as np
import matplotlib.pyplot as plt
from FDwavePY.Sources.Source import Source


class MomentTensor(Source):
    def __init__(self):
        self.kind = 'MomentTensor'
        # Source.__init__(self, name=None, 
        #                 freq=None, dt=0.001, T=1, t0=0, scale=1)
        
        raise NotImplementedError('MT type source not implemented yet.')
