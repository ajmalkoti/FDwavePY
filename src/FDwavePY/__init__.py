from  FDwavePY.Models import Models
from  FDwavePY.Sources import Sources
# from  FDwavePY.Sources import Signature


class FDwavePY(Models):
    def __init__(self,**kwargs):
        Models.__init__(self,**kwargs)
        Sources.__init__(self,**kwargs)
        
        
        
    