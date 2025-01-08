#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:47:53 2024

@author: ajay
"""
import numpy as np


def CollocatedD1_O2(arr):
    pass

def CollocatedD2_O2(arr):
    coeff = np.array([1, -2, 1])
    
    der = np.zeros_like(arr)
    der[1:-1] = coeff[0]*arr[0:-2]  + \
                coeff[1]*arr[1:-1] + \
                coeff[0]*arr[2:]
    return der


class Derivative:
    def __init__(self, grid=None, order=None, accuracy=None):
        self.grid = grid
        self.order = order
        self.accuracy = accuracy
        
        self.coeff = None
              
        
    def choose_derivative(self, grid, order, accuracy):
        self.grid = grid
        self.order = order
        self.accuracy = accuracy
        
        if grid == 'collocated':
            self.set_coeff_collocated()
            
        elif grid == 'staggered':
            self.set_coeff_staggered()
        
    def set_coeff_collocated(self):
        if self.order == 1:            
            if self.accuracy ==2: 
                self.coeff = np.array([-1/2,	0, 1/2])
                    
            elif self.accuracy ==4: 
                self.coeff = np.array([1/12, -2/3, 0, 2/3, -1/12 ])
                    
            elif self.accuracy ==6: 
                self.coeff = np.array([-1/60,3/20,-3/4,0,3/4,-3/20,1/60 ])
                    
            elif self.accuracy ==8: 
                self.coeff = np.array([1/280,-4/105,1/5,-4/5,0,4/5,-1/5,4/105,-1/280])
                    


        elif self.order == 2:            
            if self.accuracy ==2: 
                self.coeff = np.array([1, -2, 1])
                
            elif self.accuracy == 4: 
                self.coeff = np.array([-1/12, 4/3, -5/2, 4/3, -1/12 ])
            
            elif self.accuracy == 6: 
                self.coeff = np.array([1/90, -3/20, 3/2, -49/18,	3/2, -3/20, 	1/90])
                    
            elif self.accuracy == 8: 
                self.coeff = np.array([-1/560, 8/315, -1/5, 8/5, -205/72, 8/5, -1/5, 	8/315, -1/560])        
        else: 
            raise ValueError('At present only 1, 2nd order derivative are available.')
            
            
        
        
    def set_coeff_staggered(self):        
        if self.order == 1:            
            if self.accuracy ==4: 
                self.coeff = np.array([1, -27, 27, -1])/24
                    
            elif self.accuracy ==6: 
                self.coeff = np.array([-3/640, 25/384, -75/64,  75/64,  -25/384, 3/640])
                    
            elif self.accuracy ==8: 
                self.coeff = np.array([1225/1024, -245/3072, 49/5120, -5/7168])
                    
            else: 
                raise ValueError('Derivative accuray for 4/6/8  only available.')
        else: 
            raise ValueError('At present only 1st order staggered derivative is available.')
            
            
            
    def calc_derivative_1d(self, vec):        
        der = np.zeros_like(vec)
        idx = np.arange(0, vec.size - self.accuracy)
        a = self.accuracy//2        
        for i in range(self.coeff.size):
            der[a:-a] += self.coeff[i]*vec[ idx+i]
        return der
    
       
    
    def calc_derivative(self, arr, axis='x'):
        D = {'x':1, 'z':0}
        if arr.ndim ==1:
            der = self.calc_derivative_1d(arr)
        elif arr.ndim ==2:
            der = np.apply_along_axis(self.calc_derivative_1d, D[axis], arr)
        
        return  der
            
    
    
if __name__ == "__main__"    :
    d= Derivative()
    
    # check collocated derivative
    d.choose_derivative('collocated', 2, 2)
    
    # x = np.arange(21)
    # y = d.calc_derivative_1d(x*x)
    # print(y)
    
    
    x = np.arange(10)
    y = np.tile(x*x, (10,1))
    yd = d.calc_derivative_1d(y[1,:])
    ydx = d.calc_derivative(y, axis='x')
    ydz = d.calc_derivative(y, axis='z')