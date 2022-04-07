#!/usr/bin/env python
# coding: utf-8

import os
import matplotlib.pyplot as plt
import numpy as np
import expression
from settings import *

expression.method = "analytic"

def delta(dis, geo, siz, edg, modprm):
    modfun = dismodfun[dis]
    d = modprm['d']
    r = np.linspace(0, 1e-5/np.sqrt(d), 100)
    dr = np.gradient(r)
    MMMM = eval('expression.'+modfun)(r, geo, siz, edg, modprm)[0]
    dMMMM = np.gradient(MMMM, axis=1)
    dMppdr, dMmpdr, dMpmdr, dMmmdr = dMMMM/dr
    sw = d/2 * (dMppdr + dMpmdr + dMmmdr + dMmpdr) / (2*np.pi*r)
    T = sw/(d**2)-1
    r = r[2:-2]
    T = T[2:-2]
    #plt.plot(r, T)
    #plt.show()
    a, b = np.polyfit(r, T, 1)
    return b

print(delta('RDD', 'square', 1000, 'NEC', {'d': 5e-5}))

M = np.linspace(np.sqrt(2), 20, 100)

edgcon = 'GBB'
geo = 'square'
d = 5e-5

defmodprm = {
    'RRDD-E': {'d': d, 'v': 'E'},
    'RRDD-R': {'d': d, 'v': 'R'},
    'RCDD-E': {'d': d, 'v': 'E'},
    'RCDD-R': {'d': d, 'v': 'R'},
}

for dis in ['RRDD-E', 'RRDD-R', 'RCDD-E', 'RCDD-R']:

    s = M/np.sqrt(d)

    x = M
    
    modprm = defmodprm[dis]
    y = [delta(dis, geo, 1000, edgcon, dict(modprm, s=s_)) for s_ in s]

    plt.cla()
    plt.plot(x, y)
    plt.xlabel(r"$ s \sqrt{\rho} $")
    plt.ylabel(r"$ \delta $")
    plt.grid()
    plt.title(dis)
    #plt.show()
    plt.savefig(f'../plots/delta_{dis}.pdf')
