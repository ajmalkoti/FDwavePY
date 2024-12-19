import FDwavePY as sim
import numpy as np


# # update the model/source/etc parts
# s = sim.FDwavePY(rheo='sc', dim=1)        # initialize the structure
# s.mod.homogeneous(vp=2000, nodes=200, dh=1)        # define the model 
# print(s.mod.vp)
# s.mod.plot()



s = sim.FDwavePY(rheo='ac', dim=1)        # initialize the structure
s.mod.homogeneous(2000, 1200, 200)        # define the model 
print(s.mod.vp)
print(s.mod.rho)
s.mod.plot()


s.mod.vp[0:s.mod.nodes//2] = np.ones(s.mod.nodes//2)*1000
s.mod.rho[0:s.mod.nodes//2] = np.ones(s.mod.nodes//2)*900
s.mod.plot(overlay= False)


