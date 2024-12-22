from  FDwavePY.Models import Models
from  FDwavePY.Sources import Sources
# from  FDwavePY.Sources import Signature

from FDwavePY.Layout import Layout

class FDwavePY(Models):
    def __init__(self,**kwargs):
        Models.__init__(self,**kwargs)
        Sources.__init__(self,**kwargs)
        dim = kwargs.get('dim', None)
        Layout.__init__(self, dim )
    
        
        
    