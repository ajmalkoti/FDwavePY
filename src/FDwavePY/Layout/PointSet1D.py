#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 23:42:04 2024

@author: ajay
"""
import numpy as np 
import matplotlib.pyplot as plt


class PointSet1D:
    def __init__(self, locx):
        self.locx  = np.array(locx) 

    # @property
    # def npoints(self):
    #     return self.locx.size
        
    def plot(self, fig=None, ax=None, y=1, **kwargs):
        if fig is None or ax is None:
            fig, ax = plt.subplots(1,1)
            
        yy = np.ones_like(self.locx)*y
        ax.plot(self.locx, yy, **kwargs)
        
        ax.set_yticklabels('')
        ax.set_xlabel('x [m]')
        ax.spines[['left', 'right', 'top']].set_visible(False)
        ax.tick_params(left=False)
        
    
if __name__ == "__main__":    
    x = PointSet1D(5, '')
    x.plot(marker='v', c='b')
    
    x.plot(marker='*', c='r')
    
    x = PointSet1D([5,10, 15], '')
    x.plot(marker='v', c='b')