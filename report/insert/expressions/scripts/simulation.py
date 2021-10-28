#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
from lpa.input import models, sets, analyze

fun = ('MMMM', 'KKKK', 'gggg', 'GaGs')
pth = "../saved/"

n = 16000

def smart_load(r, geo, siz, dismod, modprm, edgcon):
    modstr = dismod.__name__
    if 'v' in modprm:
        modstr += '-'+modprm['v']
    prestm = str(len(r))+'_'+str(int(np.max(r)))+'_'+str(n)+'_'
    fM = pth+prestm+geo+'_MMMM_'+modstr+'_'+edgcon+'.txt'
    fK = pth+prestm+geo+'_KKKK_'+modstr+'_'+edgcon+'.txt'
    fg = pth+prestm+geo+'_gggg_'+modstr+'_'+edgcon+'.txt'
    fG = pth+prestm+geo+'_GaGs_'+modstr+'_'+edgcon+'.txt'
    if os.path.exists(fM):
        MMMM = np.loadtxt(fM)
        KKKK = np.loadtxt(fK)
        gggg = np.loadtxt(fg)
        GaGs = np.loadtxt(fG)
    else:
        s = sets.Sample(n, geo, siz, dismod, modprm, S=0)
        res = analyze.calculate(fun, s, r, ec=edgcon)
        MMMM, KKKK, gggg, GaGs = res
        np.savetxt(fM, MMMM)
        np.savetxt(fK, KKKK)
        np.savetxt(fg, gggg)
        np.savetxt(fG, GaGs)
    return MMMM, KKKK, gggg, GaGs

def RDD(r, geo, siz, edgcon, modprm):
    return smart_load(r, geo, siz, models.RDD, modprm, edgcon)

def RRDD(r, geo, siz, edgcon, modprm):
    return smart_load(r, geo, siz, models.RRDD, modprm, edgcon)
