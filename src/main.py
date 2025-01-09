import FDwavePY as sim
import numpy as np 
import matplotlib.pyplot as plt


############ TEST 1D scalar #####################
s = sim.FDwavePY(rheo='sc', dim=1, skind='Point')    
s.mod.homogeneous(vp=1500, nodes=200, dh=2)   
s.mod.plot()
s.mod.vp.ax1.get_index(8)
s.mod.vp.ax1.get_index([8,10,12])
########
s.src.ricker(freq=20, dt=0.001, T=1, t0=.05, scale=1)
s.src.plot(xlim = [0,.2])
########
vec = s.mod.vp.ax1.vec
N = len(vec)
s.layout.predef_snrn_fixed(sloc=[vec[N//2]], 
                            rloc=s.mod.vp.ax1.vec)
s.layout.plot(figsize = [4,1])
# ########
# s.simulate_ishot(0)
# s.sim.plot_receiver_response()



############ TEST 2D scalar #####################
s = sim.FDwavePY(rheo='sc', dim=2, skind='Point')    
s.mod.homogeneous(vp=1500, nodes=(200, 300), dh=2)   
s.mod.plot()
s.mod.vp.ax1.get_index(8)
s.mod.vp.ax1.get_index([8,10,12])


########
s.src.ricker(freq=20, dt=0.0005, T=1, t0=.05, scale=1)
s.src.plot(xlim = [0,.2])


########
rx = s.mod.vp.ax1.vec
rz = 2*np.ones_like(rx)

sx = [s.mod.vp.ax1.vec[150]]
sz = [s.mod.vp.ax2.vec[100]]

s.layout.predef_snrn_fixed(slocx=sx, slocz=sz,  rlocx=rx, rlocz=rz)
s.layout.plot(figsize = [4,1])

# s.layout.src[0].locx
# s.layout.src[0].locz


#%%
# ########
s.verbose = True
s.simulate_ishot(0)
s.sim.plot_receiver_response(figsize=(5,8))
# plt.imshow(s.sim.ss)
# plt.plot(ss[:,150])










