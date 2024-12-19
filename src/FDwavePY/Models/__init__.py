import numpy as np
import matplotlib.pyplot as plt
from FDwavePY.Models.Scalar1d import Scalar1d 
from FDwavePY.Models.Acoustic1d import Acoustic1d        


class Models:
    def __init__(self, **kwargs):
        name = kwargs.get('name', 'None (default)')
        rheo = kwargs.get('rheo', '')
        dim = kwargs.get('dim', None)                
        
        if rheo.lower() in ['sc', 'scalar'] :
            if dim == 1:                
                self.mod = Scalar1d(name)
        
            elif dim == 2:
                pass         
            elif dim == 3:
                pass
            
        
        #####################################################
        elif rheo.lower() in ['ac', 'acoustic'] :
            if dim == 1:                
                self.mod = Acoustic1d(name)
            elif dim == 2:
                pass
            elif dim == 3: 
                pass        


        #####################################################
        elif rheo.lower() in ['el', 'elastic'] :
            if dim == 1:
                pass            
            elif dim == 2:
                pass
            elif dim == 3: 
                pass
        
        elif rheo.lower() in ['ani', 'anisotropic'] :
            if dim == 1:
                pass            
            elif dim == 2:
                pass
            elif dim == 3: 
                pass
        
        elif rheo.lower() in ['vac', 'viscoacoustic'] :
            if dim == 1:
                pass            
            elif dim == 2:
                pass
            elif dim == 3: 
                pass
            
        elif rheo.lower() in ['vel', 'viscoelastic'] :
            if dim == 1:
                pass            
            elif dim == 2:
                pass
            elif dim == 3: 
                pass
            
        elif rheo.lower() in ['vani', 'viscoanisotropic'] :
            if dim == 1:
                pass            
            elif dim == 2:
                pass
            elif dim == 3: 
                pass


        
        else:
            raise ValueError('Name and dim can not be empty')
        
    
            
        