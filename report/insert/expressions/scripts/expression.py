#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
from lpa.input import overlap, analyze, notation

method = 'interpolation'

def EAcc(*args):
    if method == 'interpolation':
        return overlap.mean_circle_circle_interpolation(*args)
    elif method == 'analytic':
        return overlap.mean_circle_circle_analytic(*args)

def EAcs(*args):
    if method == 'interpolation':
        return overlap.mean_circle_square_interpolation(*args)
    elif method == 'analytic':
        return overlap.mean_circle_square_analytic(*args)

def Aroi_Broi_dr(r, geo, siz):
    if geo == 'square':
        Aroi = siz**2
        Broi = EAcs(r, siz)
    elif geo == 'circle':
        Aroi = np.pi*siz**2
        Broi = EAcc(r, siz)
    dr = np.gradient(r)
    Broi[0] = np.nan
    return Aroi, Broi, dr

def KKKK_gggg_GaGs(MMMM, r, d, dr, Aroi):
    KKKK = np.concatenate((2*MMMM[0:2]/d, 2*MMMM[2:4]/d))
    gggg = np.gradient(KKKK, axis=1)/(2*np.pi*r*dr)
    for i in range(4):
        gggg[i][0], gggg[i][-1] = None, None
    dMMMM = np.gradient(MMMM, axis=1)
    dMppdr, dMmpdr, dMpmdr, dMmmdr = dMMMM/dr
    Ga = Aroi*d/2*(dMppdr-dMpmdr) + Aroi*d/2*(dMmmdr-dMmpdr)
    Gs = Aroi*d/2*(dMppdr+dMpmdr) + Aroi*d/2*(dMmmdr+dMmpdr)
    GaGs = np.stack((Ga, Gs))
    return KKKK, gggg, GaGs

def RDD(r, geo, siz, edgcon, kwargs):
    Aroi, Broi, dr = Aroi_Broi_dr(r, geo, siz)
    d = kwargs['d']
    Mab = d/2*Broi
    Maa = (d/2-1/Aroi) * Broi
    MMMM = np.stack((Maa, Mab, Mab, Maa))
    if edgcon == 'WOA':
        MMMM = MMMM * np.pi*r**2/Broi
    elif edgcon == 'GBB':
        MMMM = MMMM + d/2*(np.pi*r**2-Broi)
    KKKK, gggg, GaGs = KKKK_gggg_GaGs(MMMM, r, d, dr, Aroi)
    if edgcon in ('NEC', 'GBB'):
        Ga = -d*np.gradient(Broi)/dr
    elif edgcon == 'WOA':
        Ga = -2*d*np.pi*r
    Ga[0], Ga[-1] = None, None
    GaGs = np.stack((Ga, GaGs[1]))
    return (MMMM, KKKK, gggg, GaGs)

def RRDD(r, geo, siz, edgcon, kwargs):
    Aroi, Broi, dr = Aroi_Broi_dr(r, geo, siz)
    d = kwargs['d']
    s = kwargs['s']
    EA = EAcs(r, s)
    f = round(d*s**2)
    if kwargs['v'] == 'E':
        tau_ab = f/2
        tau_aa = f/2
        eta_ab = f/2
        eta_aa = f/2 - 1
        if edgcon in ('NEC', 'GBB'):
            Ga = -d*Aroi/s**2*np.gradient(EA)/dr
        elif edgcon == 'WOA':
            Ga = -d*Aroi/s**2*np.gradient(EA*np.pi*r**2/Broi)/dr
    elif kwargs['v'] == 'R':
        tau_ab = s**2/(Aroi-s**2)*(d/2*Aroi - f/2 + 1/2)
        tau_aa = s**2/(Aroi-s**2)*(d/2*Aroi - f/2 - 1/2)
        eta_aa = (f-1)/2
        eta_ab = (f-1)/2
        if edgcon in ('NEC', 'GBB'):
            Ga = d*Aroi/(Aroi-s**2)*np.gradient(EA-Broi)/dr
        elif edgcon == 'WOA':
            Ga = d*Aroi/(Aroi-s**2)*np.gradient(EA/Broi -np.pi*r**2)/dr
    Mab = ((eta_ab-tau_ab)*EA + tau_ab*Broi)/s**2
    Maa = ((eta_aa-tau_aa)*EA + tau_aa*Broi)/s**2
    MMMM = np.stack((Maa, Mab, Mab, Maa))
    if edgcon == 'WOA':
        MMMM = MMMM * np.pi*r**2/Broi
    elif edgcon == 'GBB':
        MMMM = MMMM + d/2*(np.pi*r**2-Broi)
    KKKK, gggg, GaGs = KKKK_gggg_GaGs(MMMM, r, d, dr, Aroi)
    GaGs = np.stack((Ga, GaGs[1]))
    return (MMMM, KKKK, gggg, GaGs)

def energy(r0, siz, modfun, modprm, geo, edgcon):
    if edgcon == 'NEC':
        if geo == 'circle':
            k = 2
        elif geo == 'square':
            k = np.sqrt(2)
        N = round(k*siz/r0) + 2
    elif edgcon == 'WOA':
        k, N = 1, 100
    r = np.linspace(r0, k*siz, N)
    Aroi, Broi, dr = Aroi_Broi_dr(r, geo, siz)
    # Es
    if edgcon == 'NEC':
        f = 1/(2*np.pi*r**2)
        ei = np.zeros(len(r))
        for i in range(len(r)):
            ei[i] = np.trapz(f[i:], Broi[i:])
        Es = ei[0]
    elif edgcon == 'WOA':
        ei = np.log(siz/r)
        Es = np.log(siz/r0)
    # Ei
    Ga = modfun(r, geo, siz, edgcon, modprm)[-1][0]
    Ga[0], Ga[-1] = Ga[1], Ga[-2]
    Ei = np.trapz(Ga*ei, r)/modprm['d']/Aroi
    # Et
    Et = Es + Ei
    return np.array((Es, Ei, Et))

def energies(r0, R, modfun, modprm, geo, edgcon):
    modstr = modfun.__name__+notation.parameters(modprm, c='stm')
    if 'v' in modprm:
        modstr += '-'+modprm['v']
    pth = (f"../saved/{method}_energies_{edgcon}_{modstr}_{geo}_"
           f"R_{R[0]:1.0f}_{R[-1]:1.0f}_{len(R)}.txt")
    if os.path.exists(pth):
        return np.loadtxt(pth)
    res = np.zeros((len(R), 3))
    for i in range(len(R)):
        res[i] = energy(r0, R[i], modfun, modprm, geo, edgcon)
    np.savetxt(pth, res)
    return res
