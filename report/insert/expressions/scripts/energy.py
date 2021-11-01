#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import expression
import scipy.integrate
import math
from lpa.input import overlap, notation

dst = 5e-4 # nm^-2
r0 = 1 # nm
rM = 2000 # nm
R = np.linspace(10*r0, rM, 100)

geoxax = {
    'circle': '$R_{ROI}$ (nm)',
    'square': '$S_{ROI}$ (nm)',
}
geoAroi = {
    'circle': np.pi*R**2,
    'square': R**2,
}
disord = (
    'RDD',
    'RRDD-E',
    'RRDD-R',
)
edgconord = (
    'NEC',
    'WOA',
)
edgcongeo = {
    'NEC': ('circle', 'square'),
    'WOA': ('circle',),
}
edgconlbl = {
    'NEC': (r"\int_{r=r_0}^{+\infty} \frac{1}{2 \pi r^2} d \mathcal{B}_{ROI} (r)",
            r"\frac{1}{\rho \mathcal{A}_{ROI}} \int_{r=r_0}^{+\infty} G_A^{NEC} (r) \int_{x=r}^{+\infty} \frac{1}{2 \pi x^2} d \mathcal{B}_{ROI} (x) dr"),
    'WOA': (r"\ln \left( \frac{R_{ROI}}{r_0} \right)",
            r"\frac{1}{\rho \mathcal{A}_{ROI}} \int_{r=r_0}^{R_{ROI}} G_A^{WOA} (r) \ln \left( \frac{R_{ROI}}{r} \right) dr"),
}
dismodprm = {
    'RDD': {'d': dst},
    'RRDD-E': {'d': dst, 's': 200, 'v': 'E'},
    'RRDD-R': {'d': dst, 's': 200, 'v': 'R'},
}
dismodfun = {
    'RDD': expression.RDD,
    'RRDD-E': expression.RRDD,
    'RRDD-R': expression.RRDD,
}

for dis in disord:
    for edgcon in edgconord:
        for geo in edgcongeo[edgcon]:
            modfun = dismodfun[dis]
            modprm = dismodprm[dis]
            args = (r0, R, modfun, modprm, geo, edgcon)
            Es, Ei, Et = expression.energies(*args).T
            lbs, lbi = edgconlbl[edgcon]
            plt.plot(R, Es, label=f"$e_S^{{{edgcon}}} = {lbs}$")
            plt.plot(R, Ei, label=f"$e_I^{{{edgcon}}} = {lbi}$")
            plt.plot(R, Et, label=f"$e_T^{{{edgcon}}} = e_S^{{{edgcon}}} + e_I^{{{edgcon}}}$")
            if dis=='RDD' and edgcon=='WOA':
                Re = R/np.sqrt(np.e)
                plt.plot(
                    R,
                    np.log(Re/r0),
                    '.',
                    label=r"$\ln \left( \frac{R_{ROI}}{\sqrt{e} r_0} \right)$",
                )
            plt.legend()
            plt.grid()
            plt.xlabel(geoxax[geo])
            plt.title(f"{modfun.__name__+notation.parameters(modprm, c='ttl')} {geo} {edgcon} ($ r_0 = {r0} $ nm)")
            plt.savefig(f"../plots/{geo}_{dis}_energy_{edgcon}.pdf")
            plt.clf()
