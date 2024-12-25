#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 14:47:40 2024

@author: ajay
"""

class BC1D:
    def __init__(self):
        """
        By default all BC are reflecting
        """
        self.left = 'r'
        self.right = 'r'
        
    def set_abc(self, edges, kind, **kwargs):        
        if kind == 'absorb':
            