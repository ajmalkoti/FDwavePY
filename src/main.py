import FDwavePY as sim
import numpy as np 
import matplotlib.pyplot as plt


############ TEST 1D scalar #####################
# s = sim.FDwavePY(rheo='sc', dim=1, skind='Point')    
# s.mod.homogeneous(vp=1500, nodes=200, dh=2)   
# s.mod.plot()
# s.mod.vp.ax1.get_index(8)
# s.mod.vp.ax1.get_index([8,10,12])
# ########
# s.src.ricker(freq=20, dt=0.001, T=1, t0=.05, scale=1)
# s.src.plot(xlim = [0,.2])
# ########
# vec = s.mod.vp.ax1.vec
# N = len(vec)
# s.layout.predef_snrn_fixed(sloc=[vec[N//2]], 
#                             rloc=s.mod.vp.ax1.vec)
# s.layout.plot()
# ########
# ss = s.simulate_ishot(0)
# plt.imshow(ss)



############ TEST 2D scalar #####################
s = sim.FDwavePY(rheo='sc', dim=2, skind='Point')    
s.mod.homogeneous(vp=1500, nodes=(200, 300), dh=2)   
s.mod.plot()
s.mod.vp.ax1.get_index(8)
s.mod.vp.ax1.get_index([8,10,12])


########
s.src.ricker(freq=20, dt=0.001, T=1, t0=.05, scale=1)
s.src.plot(xlim = [0,.2])


########
rx = s.mod.vp.ax1.vec
rz = np.ones_like(rx)

N = rx.size
sx = [rx[N//2]]
sz = np.ones_like(sx)


s.layout.predef_snrn_fixed(slocx=sx, slocz=sz,  rlocx=rx, rlocz=rz)
s.layout.plot()
# ########
ss = s.simulate_ishot(0)
# # plt.imshow(ss)

## TODO fix 2d simulation for 2D derivative.








