#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 23:42:04 2024

@author: ajay
"""
import numpy as np 
import matplotlib.pyplot as plt


class PointSet2D:
    def __init__(self, locx, locz):
        self.locx  = np.array(locx) 
        self.locz  = np.array(locz) 

    # @property
    # def npoints(self):
    #     if self.locx.size == self.locz.size: 
    #         return self.locx.size
        
    def plot(self, fig=None, ax=None, y=None, **kwargs):
        if fig is None or ax is None:
            fig, ax = plt.subplots(1,1)
            
        if y is None:
            yy =self.locz
        else:
            yy = np.ones_like(self.locx)*y
            
        ax.plot(self.locx, yy, **kwargs)
        
        ax.set_yticklabels('')
        ax.set_xlabel('x [m]')
        ax.spines[['left', 'right', 'top']].set_visible(False)
        ax.tick_params(left=False)
        
    
if __name__ == "__main__":    
    x = PointSet2D(5,10)
    x.plot(marker='v', c='b')
    
    x.plot(marker='*', c='r')
    
    x = PointSet2D([5,10, 15], [1,1,1])
    x.plot(marker='v', c='b')
    x.plot(marker='*', c='r')