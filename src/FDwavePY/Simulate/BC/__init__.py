#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 15:01:49 2024

@author: ajay
"""

class BC:
    def __init__(self):
        self.left = 'reflect'
        self.right= 'reflect'
        
    @property 
    def left(self):
        return self._left
    
    @left.setter
    def left(self, val):
        if val in ['reflect', 'damp', 'pml']:
            self._left = val
        else:
            raise ValueError('BC type is not in database.')
            
            
    @property 
    def right(self):
        return self._right
    
    @right.setter
    def right(self, val):
        if val in ['reflect', 'damp', 'pml']:
            self._right = val
        else:
            raise ValueError('BC type is not in database.')
            
    
    def set_bc(self, left, right):        
        self.left = left
        self.right= right
        
        