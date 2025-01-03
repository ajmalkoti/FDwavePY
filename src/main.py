import FDwavePY as sim
import numpy as np


## update the model/source/etc parts
# s = sim.FDwavePY(rheo='sc', dim=1)        # initialize the structure
# s.mod.homogeneous(vp=2000, nodes=200, dh=1)        # define the model 
# s.mod.plot()


# s = sim.FDwavePY(rheo='ac', dim=1)        # initialize the structure
# s.mod.homogeneous(2000, 1200, 200)        # define the model 
# print(s.mod.vp)
# print(s.mod.rho)
# s.mod.plot()


# s.mod.vp[0:s.mod.nodes//2] = np.ones(s.mod.nodes//2)*1000
# s.mod.rho[0:s.mod.nodes//2] = np.ones(s.mod.nodes//2)*900
# s.mod.plot(overlay= True)
# s.mod.plot(overlay= False)



# s = sim.FDwavePY(rheo='el', dim=1)        # initialize the structure
# s.mod.homogeneous(2000, 1800, 1200, 200)        # define the model 
# s.mod.plot(overlay= True)
# s.mod.plot(overlay= False)


# s = sim.FDwavePY(rheo='vac', dim=1)        # initialize the structure
# s.mod.homogeneous(2000, 1200, 80, 200)        # define the model 
# s.mod.plot(overlay= True)
# s.mod.plot(overlay= False)



# s = sim.FDwavePY(rheo='vel', dim=1)        # initialize the structure
# s.mod.homogeneous(2000, 1800, 1200, 80, 60, 200)        # define the model 
# s.mod.plot(overlay= True)
# s.mod.plot(overlay= False)


# s = sim.FDwavePY(rheo='vel', dim=1)        # initialize the structure
# s.mod.homogeneous(2000, 1800, 1200, 80, 60, 200)        # define the model 
# s.mod.plot(overlay= True)
# s.mod.plot(overlay= False)




##################################
### SOURCE SIGNATURE
##################################
# s = sim.FDwavePY(rheo='sc', dim=1, skind='Point')        # initialize the structure
# s.src.ricker()
# s.src.plot()


# s.src.sine()
# s.src.plot(title='Sine wavelet')

# s.src.triangle()
# s.src.plot()




##################################
### LAYOUT OF SOURCE AND RECEIVER
##################################
# s = sim.FDwavePY(rheo='sc', dim=1, skind='Point')        # initialize the structure
# s.layout.add_src_rec(5, 10)
# s.layout.plot()


# s.layout.add_src_rec([2,4,6], 10)
# s.layout.plot()

# s.layout.add_src_rec(1, [6,8,10])
# s.layout.plot()


# s.layout.add_src_rec([2,4,6], [10,12,14])
# s.layout.plot()


# s.layout.predef_s1r1(5, 10)
# s.layout.plot()      

# s.layout.predef_s1rn(5, [10, 15, 20, 25, 30, 35])
# s.layout.plot()


# s.layout.predef_snrn_fixed([5, 10, 15, 20],   [10, 15, 20, 25, 30, 35])
# s.layout.plot()


# s.layout.predef_snrn_rollover([5, 10, 15, 20], [10, 12, 14, 16,18, 20], rroll=5)
# s.layout.plot()





##################################
### Simulation 
##################################
s = sim.FDwavePY(rheo='sc', dim=1, skind='Point')    
s.mod.homogeneous(vp=2000, nodes=200, dh=1)        # define the model 
# s.mod.plot()


# s.src.ricker()
# # s.src.plot()

# s.layout.add_src_rec(5, 10)
# s.layout.plot()



# s.der.set_coeff(grid='collocated', order=2, accuracy=2)
# print(s.der.coeff)


# # s.bc.set_bc(left='reflect',  right='damp')
# # s.simulate()


# #########################
# vp = s.mod.vp
# dh = s.mod.dh 

# sig =  s.src.svec
# dt = s.src.dt
# nt = s.src.nt


# sloc = s.layout.src
# rloc = s.layout.rec


# s.check_stability()
# s.check_dispersion()

# bc = [s.bc.left, s.bc.right]

# vpe = s.expand_domain(vp, left=2, right=5)

# s.correct_src_rec_loc(sloc, left=2, right=5)
 

# for i in range(nt):
    
#     s.der.calc_derivative_1d(vp)




