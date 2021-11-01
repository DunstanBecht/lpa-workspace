#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import expression

edgconord = (
    'NEC',
    'WOA',
)
varord = (
    'E',
    'R',
)
edgconrad = {
    'NEC': np.linspace(1000, 2000, 21),
    'WOA': np.linspace(1000, 2000, 21),
}
dst = 5e-4 # nm^-2
geo = 'circle'
r0 = 1 # nm
s = np.linspace(100, 500, 21) # nm

for edgcon in edgconord:
    for var in varord:
        print(f"RRDD-{var} {edgcon}")
        R = edgconrad[edgcon]
        stm = (f"{geo}_RRDD-{var}_energy3D_{edgcon}_"
               f"R_{R[0]:1.0f}_{R[-1]:1.0f}_{len(R)}_"
               f"s_{s[0]:1.0f}_{s[-1]:1.0f}_{len(s)}.txt")
        ttl = f"RRDD-E {geo} {edgcon}"

        # load or compute
        X, Y = np.meshgrid(R, s)
        if stm in os.listdir("../saved"):
            Z = np.loadtxt(os.path.join("../saved", stm))
        else:
            print(R)
            print(s)
            def fun3D(x, y):
                print(f"R: {x:4.0f}nm     s: {y:4.0f}nm")
                modprm = {'d': dst, 's': y, 'v': var}
                args = (r0, x, expression.RRDD, modprm, geo, edgcon)
                Es, Ei, Et = expression.energy(*args).T
                return Et
            fun3Dvec = np.vectorize(fun3D)
            Z = fun3Dvec(X, Y)
            np.savetxt(os.path.join("../saved", stm), Z)

        # plot settings
        plt.figure(figsize=(7, 5))
        ax = plt.axes(projection='3d')
        plt.rcParams['axes.titley'] = 1.0
        plt.subplots_adjust(
            left=0,
            bottom=0,
            right=1,
            top=1,
            wspace=0,
            hspace=0,
        )
        ax.view_init(elev=20, azim=-135)
        
        # plot energy
        ax.plot_surface(
            X,
            Y,
            Z,
            cmap=cm.coolwarm,
            edgecolor=None,
        )
        ax.set_xlabel(r"$ R_{ROI} $ (nm)")
        ax.set_ylabel(r"$ s $ (nm)")
        ax.set_zlabel(r"$ e_T $")
        plt.title(ttl)
        plt.savefig(f"../plots/{geo}_RRDD-{var}_energy3D_{edgcon}.pdf")

        plt.cla()

        # plot effective cut-off radius
        ax.plot_surface(
            X,
            Y,
            r0*np.exp(Z),
            cmap=cm.coolwarm,
            edgecolor=None,
        )
        ax.set_xlabel(r"$ R_{ROI} $ (nm)")
        ax.set_ylabel(r"$ s $ (nm)")
        ax.set_zlabel(r"$ R_e = r_0 \exp \left( e_T \right) $")
        plt.title(ttl)
        plt.savefig(f"../plots/{geo}_RRDD-{var}_cutrad3D_{edgcon}.pdf")
