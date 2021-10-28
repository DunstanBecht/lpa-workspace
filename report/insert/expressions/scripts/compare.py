#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import matplotlib.pyplot as plt
import simulation
import expression
from lpa.input import notation

a, b, n = 0.01, 3000, 70

geoord = (
    #'circle',
    'square',
)
geoedgord = {
    'circle': ('NEC', 'WOA'),
    'square': ('NEC', 'WOA', 'GBB'),
}
disord = (
    'RDD',
    'RRDD-E',
    'RRDD-R',
)
metord = (
    'simulation',
    'expression',
)
funord = {
    #"M": (0, {"++": 0, "+-": 1}),
    #"K": (1, {"++": 0, "+-": 1}),
    "g": (2, {"++": 0, "+-": 1}),
    "Ga": (3, {"A": 0}),
}

geosiz = {
    'circle': 1000,
    'square': 2000,
}
metmrk = {
    'simulation': '-',
    'expression': '.',
}
metrad = {
    'simulation': np.linspace(a, b, 2*n),
    'expression': np.linspace(a, b, n-1),
}
dismodprm = {
    'RDD': {'d': 5e-5},
    'RRDD-E': {'d': 5e-5, 's': 200, 'v': 'E'},
    'RRDD-R': {'d': 5e-5, 's': 200, 'v': 'R'},
}
dismodfun = {
    'RDD': 'RDD',
    'RRDD-E': 'RRDD',
    'RRDD-R': 'RRDD',
}

for dis in disord:
    for geo in geoord:
        for edg in geoedgord[geo]:
            for fun in funord:
                for sub in funord[fun][1]:
                    for met in metord:
                        siz = geosiz[geo]
                        modfun = dismodfun[dis]
                        modprm = dismodprm[dis]
                        rad = metrad[met]
                        mrk = metmrk[met]
                        res = eval(met+'.'+modfun)(rad, geo, siz, edg, modprm)
                        i = funord[fun][0]
                        j = funord[fun][1][sub]
                        col = 'C'+str(j)
                        lab = "$\mathrm{"+fun+"}^{"+edg+"}_{"+sub+"}$ "+met
                        plt.plot(rad, res[i][j], mrk, label=lab, color=col)
                plt.title(modfun+notation.parameters(modprm, c='ttl')+" "+geo+" "+str(siz)+"nm")
                plt.xlabel(r"$r$ (nm)")
                plt.legend()
                plt.grid()
                print('_'.join((geo, dis, fun, edg)))
                plt.savefig("../plots/"+'_'.join((geo, dis, fun, edg))+'.pdf')
                plt.clf()
