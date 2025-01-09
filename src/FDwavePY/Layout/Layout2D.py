#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:31:24 2024

@author: ajay
"""

import numpy as np 
import matplotlib.pyplot as plt
try : 
    from FDwavePY.Layout.PointSet2D import PointSet2D
except ImportError:
    from PointSet2D import PointSet2D



class Layout2D(): 
    def __init__(self):
        self.src = []
        self.rec = []
        
    def add_src_rec(self, slocx, slocz, rlocx, rlocz):
        self.src.append(PointSet2D(slocx, slocz))
        self.rec.append(PointSet2D(rlocx, rlocz))
        
    
    def plot(self, fig=None, ax=None, yscale=1, figsize=None):
        if ax is None or fig is None:
            if figsize is None:
                fig, ax = plt.subplots(1,1)
            else: 
                fig, ax = plt.subplots(1,1, figsize=figsize)      
        
        ax.set_yticklabels('')
        ax.set_xlabel('x [m]')
        ax.spines[['left', 'right', 'top']].set_visible(False)
        ax.tick_params(left=False)
        N = len(self.src)
        ax.set_ylim([-1*yscale, N*yscale])
        for i in range(N):            
            self.rec[i].plot(marker='v', c='b',y=i, fig=fig, ax=ax)
            self.src[i].plot(marker='*', c='r',y=i, fig=fig, ax=ax)
            
            
     
    def predef_s1r1(self, slocx, slocz, rlocx, rlocz):
        mylist = [slocx, slocz, rlocx, rlocz]
        for i in mylist: 
            if isinstance(i, (int, float)) :
                pass
            else:
                raise ValueError('The source & receiver locations must be of integer/float type')

        self.add_src_rec(slocx, slocz, rlocx, rlocz)
    
    
    def predef_s1rn(self, slocx,slocz,  rlocx, rlocz):
        if not isinstance(slocx, (int, float, np.integer, np.floating)) :
            raise ValueError('The slocx should be and int/float')
        
        if not isinstance(slocz, (int, float, np.integer, np.floating)) :
            raise ValueError('The slocz should be and int/float')
            
        if len(rlocx)<=1:
            raise ValueError('rlocx should be a 2D array')
            
        rlocx = np.array(rlocx)
        if not isinstance(rlocx[0], (np.integer,np.floating)):
            raise ValueError('The rlocx must be of integer type')
            
        rlocz = np.array(rlocz)
        if not isinstance(rlocz[0], (np.integer,np.floating)):
            raise ValueError('The rlocz must be of integer type')
            
        self.add_src_rec(slocx, slocz, rlocx, rlocz)
        
        
            
            
    def predef_snrn_fixed(self, slocx, slocz, rlocx, rlocz):
        slocx = np.array(slocx)
        slocz = np.array(slocz)
        
        rlocx = np.array(rlocx)
        rlocz = np.array(rlocz)
        
        for i in range(len(slocx)):
            self.predef_s1rn(slocx[i], slocz[i],  rlocx, rlocz)
            
    
    
    def predef_snrn_rollover(self, slocx, slocz, rlocx, rlocz, rroll=10):
        slocx = np.array(slocx)
        slocz = np.array(slocz)
        
        rlocx = np.array(rlocx)
        rlocz = np.array(rlocz)
        
        for i in range(len(slocx)):
            self.predef_s1rn(slocx[i], slocx[i], rlocx + i*rroll, rlocz)
            
     
        
if __name__ == "__main__":
    x = Layout2D()
    x.add_src_rec(5, 1, 10, 1)
    x.plot()
    
    x.add_src_rec([2,4,6],[1,1,1],   10,1)
    x.plot()

    x.add_src_rec(1, 1,    [6,8,10], [1,1,1])
    x.plot()

    x.add_src_rec([2,4,6], [1,1,1],   [10,12,14], [1,1,1])
    x.plot()


    x.predef_s1r1(5, 1,  10, 1)
    x.plot()      


    x.predef_s1rn(5,1,    [10, 15, 20, 25, 30, 35], [1,1,1,1,1,1])
    x.plot()


    x.predef_snrn_fixed([5, 10, 15, 20], [1,1,1, 1],  
                        [10, 15, 20, 25, 30, 35], [1, 1, 1, 1, 1, 1])
    x.plot()


    x.predef_snrn_rollover([5, 10, 15, 20], [1,1,1, 1],  
                           [10, 12, 14, 16,18, 20], [1, 1, 1, 1, 1, 1], 
                           rroll=5)
    x.plot()    