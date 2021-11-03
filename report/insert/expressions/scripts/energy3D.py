#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
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
    'NEC': np.linspace(1000, 10000, 21),
    'WOA': np.linspace(1000, 10000, 21),
}
edgcongeo = {
    'NEC': ('circle', 'square'),
    'WOA': ('circle',),
}
dst = 5e-4 # nm^-2
r0 = 1 # nm
s = np.linspace(100, 500, 21) # nm

for edgcon in edgconord:
    for geo in edgcongeo[edgcon]:
        for var in varord:
            print(f"RRDD-{var} {edgcon}")
            R = edgconrad[edgcon]
            pth = (f"../saved/{expression.method}_energy3D_{edgcon}_RRDD-{var}_{geo}_"
                   f"R_{R[0]:1.0f}_{R[-1]:1.0f}_{len(R)}_"
                   f"s_{s[0]:1.0f}_{s[-1]:1.0f}_{len(s)}.txt")
            ttl = f"RRDD-{var} {geo} {edgcon} ($ r_0 = {r0} $ nm)"

            # load or compute
            X, Y = np.meshgrid(R, s)
            if os.path.exists(pth):
                Z = np.loadtxt(pth)
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
                np.savetxt(pth, Z)

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
                cmap='plasma',
                edgecolor=None,
            )
            ax.set_xlabel(r"$ R_{ROI} $ (nm)")
            ax.set_ylabel(r"$ s $ (nm)")
            ax.set_zlabel(fr"$ e_T^{{{edgcon}}} $")
            plt.title(ttl)
            plt.savefig(f"../plots/energy3D_{edgcon}_RRDD-{var}_{geo}.pdf")

            plt.cla()

            # plot effective cut-off radius
            ax.plot_surface(
                X,
                Y,
                r0*np.exp(Z),
                cmap='plasma',
                edgecolor=None,
            )
            ax.set_xlabel(r"$ R_{ROI} $ (nm)")
            ax.set_ylabel(r"$ s $ (nm)")
            ax.set_zlabel(fr"$ R_e^{{{edgcon}}} = r_0 \exp \left( e_T^{{{edgcon}}} \right) $ (nm)")
            plt.title(ttl)
            plt.savefig(f"../plots/cutrad3D_{edgcon}_RRDD-{var}_{geo}.pdf")
