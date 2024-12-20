import numpy as np
import matplotlib.pyplot as plt
from FDwavePY.Models.Scalar1d import Scalar1d 
from FDwavePY.Models.Acoustic1d import Acoustic1d        
from FDwavePY.Models.Elastic1d import Elastic1d

from FDwavePY.Models.ViscoAcoustic1d import ViscoAcoustic1d
from FDwavePY.Models.ViscoElastic1d import ViscoElastic1d

class Models:
    def __init__(self, **kwargs):
        name = kwargs.get('name', 'None (default)')
        rheo = kwargs.get('rheo', '')
        dim = kwargs.get('dim', None)                
        
        if rheo.lower() in ['sc', 'scalar'] :
            if dim == 1:                
                self.mod = Scalar1d(name)
        
            elif dim == 2:
                raise NotImplementedError('This function is not yet implemented')         
            elif dim == 3:
                raise NotImplementedError('This function is not yet implemented')
            
        
        #####################################################
        elif rheo.lower() in ['ac', 'acoustic'] :
            if dim == 1:                
                self.mod = Acoustic1d(name)
            elif dim == 2:
                raise NotImplementedError('This function is not yet implemented')
            elif dim == 3: 
                raise NotImplementedError('This function is not yet implemented')


        #####################################################
        elif rheo.lower() in ['el', 'elastic'] :
            if dim == 1:
                self.mod = Elastic1d(name)
            elif dim == 2:
                raise NotImplementedError('This function is not yet implemented')
            elif dim == 3: 
                raise NotImplementedError('This function is not yet implemented')
        
        elif rheo.lower() in ['ani', 'anisotropic'] :
            if dim == 1:
                raise NotImplementedError('This function is not yet implemented')            
            elif dim == 2:
                raise NotImplementedError('This function is not yet implemented')
            elif dim == 3: 
                raise NotImplementedError('This function is not yet implemented')
        
        elif rheo.lower() in ['vac', 'viscoacoustic'] :
            if dim == 1:
                self.mod = ViscoAcoustic1d(name)
            elif dim == 2:
                raise NotImplementedError('This function is not yet implemented')
            elif dim == 3: 
                raise NotImplementedError('This function is not yet implemented')
            
        elif rheo.lower() in ['vel', 'viscoelastic'] :
            if dim == 1:
                self.mod = ViscoElastic1d(name)
            elif dim == 2:
                raise NotImplementedError('This function is not yet implemented')
            elif dim == 3: 
                raise NotImplementedError('This function is not yet implemented')
            
        elif rheo.lower() in ['vani', 'viscoanisotropic'] :
            if dim == 1:
                raise NotImplementedError('This function is not yet implemented')            
            elif dim == 2:
                raise NotImplementedError('This function is not yet implemented')
            elif dim == 3: 
                raise NotImplementedError('This function is not yet implemented')


        
        else:
            raise ValueError('Name and dim can not be empty')
        
    
            
        