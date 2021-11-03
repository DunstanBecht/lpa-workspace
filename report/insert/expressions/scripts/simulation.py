#!/usr/bin/env python
# coding: utf-8

import numpy as np
from lpa.input import models, notation

def smart_load(r, geo, siz, dismod, modprm, edgcon):
    stm = f"../saved/{dismod.__name__}{notation.parameters(modprm, c='stm')}_FUN_{edgcon}.txt"
    fM = stm.replace('FUN', 'MMMM')
    fK = stm.replace('FUN', 'KKKK')
    fg = stm.replace('FUN', 'gggg')
    fG = stm.replace('FUN', 'GaGs')
    MMMM = np.loadtxt(fM)
    KKKK = np.loadtxt(fK)
    gggg = np.loadtxt(fg)
    GaGs = np.loadtxt(fG)
    return MMMM, KKKK, gggg, GaGs

def RDD(r, geo, siz, edgcon, modprm):
    return smart_load(r, geo, siz, models.RDD, modprm, edgcon)

def RRDD(r, geo, siz, edgcon, modprm):
    return smart_load(r, geo, siz, models.RRDD, modprm, edgcon)
