#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:29:53 2024

@author: ajay
"""
import numpy as np 
import matplotlib.pyplot as plt

# from FDwavePY.Layout.Layout1D import Layout1D

from FDwavePY.Layout.PointSet1D import PointSet1D
# from PointSet1D import PointSet1D


class Layout1D: 
    def __init__(self):
        self.src = []
        self.rec = []
    
    def add_src_rec(self, sloc, rloc):                
        self.src.append(PointSet1D(sloc))
        self.rec.append(PointSet1D(rloc))
   
    def plot(self, fig=None, ax=None, yscale=1):
        if ax is None or fig is None:
            fig, ax = plt.subplots(1,1)        
        
        ax.set_yticklabels('')
        ax.set_xlabel('x [m]')
        ax.spines[['left', 'right', 'top']].set_visible(False)
        ax.tick_params(left=False)
        N = len(self.src)
        ax.set_ylim([-1*yscale, N*yscale])
        for i in range(N):            
            self.rec[i].plot(marker='v', c='b',y=i, fig=fig, ax=ax)
            self.src[i].plot(marker='*', c='r',y=i, fig=fig, ax=ax)
            
     
    def predef_s1r1(self, sloc, rloc):
        if isinstance(sloc, (int, float)) & isinstance(rloc, (int,float)):
            self.add_src_rec(sloc, rloc)
        else:
            raise ValueError('The source receiver must be of integer type')
    
    
    def predef_s1rn(self, sloc, rloc):
        if not isinstance(sloc, (int, float, np.integer, np.floating)) :
            raise ValueError('The sloc should be and int/float')
            
        if len(rloc)<=1:
            raise ValueError('rloc should be a 1D array')
            
        rloc = np.array(rloc)
        if not isinstance(rloc[0], (np.integer,np.floating)):
            raise ValueError('The rloc must be of integer type')
            
        self.add_src_rec(sloc, rloc)
        
        
            
            
    def predef_snrn_fixed(self, sloc, rloc):
        sloc = np.array(sloc)
        rloc = np.array(rloc)
        for i in range(len(sloc)):
            self.predef_s1rn(sloc[i], rloc)
            
    
    def predef_snrn_rollover(self, sloc, rloc, rroll=10):
        sloc = np.array(sloc)
        rloc = np.array(rloc)
        for i in range(len(sloc)):
            self.predef_s1rn(sloc[i], rloc + i*rroll)
        
        
# x = Layout1D() 
# x.add_src_rec(5, 10)
# x.plot()


# x.add_src_rec([2,4,6], 10)
# x.plot()

# x.add_src_rec(1, [6,8,10])
# x.plot()


# x.add_src_rec([2,4,6], [10,12,14])
# x.plot()


# x.predef_s1r1(5, 10)
# x.plot()      

# x.predef_s1rn(5, [10, 15, 20, 25, 30, 35])
# x.plot()


# x.predef_snrn_fixed([5, 10, 15, 20],   [10, 15, 20, 25, 30, 35])
# x.plot()


# x.predef_snrn_rollover([5, 10, 15, 20], [10, 12, 14, 16,18, 20], rroll=5)
# x.plot()