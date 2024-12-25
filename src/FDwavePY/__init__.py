from  FDwavePY.Models import Models
from  FDwavePY.Sources import Sources
# from  FDwavePY.Sources import Signature

from FDwavePY.Layout import Layout
from FDwavePY.Simulate import Simulate



class FDwavePY(Simulate):
    def __init__(self,**kwargs):
        Models.__init__(self,**kwargs)
        # Sources.__init__(self,**kwargs)
        
        # dim = kwargs.get('dim', None)
        # rheo = kwargs.get('rheo', None)
        
        # Layout.__init__(self, dim )
        # Simulate.__init__(self, dim, rheo )
    
        
        
    