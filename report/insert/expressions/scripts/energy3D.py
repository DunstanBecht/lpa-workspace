#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import expression
import scipy.integrate
import math
from lpa.input import overlap, notation

dst = 5e-4 # nm^-2
r0 = 1 # nm
geo = 'circle'
edgcon = 'NEC'
R = np.linspace(1000, 2000, 2)
s = np.linspace(100, 500, 21)

X, Y = np.meshgrid(R, s)

stm = (f"energy3D_RRDD-E_{geo}_{edgcon}_"
       f"R_{R[0]:1.0f}_{R[-1]:1.0f}_{len(R)}_"
       f"s_{s[0]:1.0f}_{s[-1]:1.0f}_{len(s)}.txt")
ttl = f"RRDD-E {geo} {edgcon}"

# load or compute
if stm in os.listdir("../saved"):
    Z = np.loadtxt(os.path.join("../saved", stm))
else:
    print(R)
    print(s)
    def fun3D(x, y):
        print(f"R: {x:4.0f}nm     s: {y:4.0f}nm")
        modprm = {'d': dst, 's': y, 'v': 'E'}
        args = (r0, x, expression.RRDD, modprm, geo, edgcon)
        Es, Ei, Et = expression.energy(*args).T
        return Et
    fun3Dvec = np.vectorize(fun3D)
    Z = fun3Dvec(X, Y)
    np.savetxt(os.path.join("../saved", stm), Z)

# plot
plt.figure(figsize=(7, 5))
plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
ax = plt.axes(projection='3d')
ax.plot_surface(
    X,
    Y,
    Z,
    cmap=cm.coolwarm,
    edgecolor=None,
    )
ax.view_init(elev=20, azim=-135)
ax.set_xlabel(r"$ R_{ROI} $ (nm)")
ax.set_ylabel(r"$s$ (nm)")
ax.set_zlabel(r"$e_T$")
plt.rcParams['axes.titley'] = 1.0
#plt.rcParams['axes.titlepad'] = -5
plt.title(ttl)
plt.savefig(f"../plots/{geo}_energy3D_{edgcon}.pdf")
