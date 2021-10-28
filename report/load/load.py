#!/usr/bin/env python
# coding: utf-8

"""
Load data.
"""

import os
import math
import numpy as np

# order of magnitude of the densities
dstexp = (
    13,
    14,
    #15,
)

# real densities [m^-2]
readst = [5*10**exp for exp in dstexp]

# distribution models order
dismodord = (
    '_RDD',
    '_RRDD-E',
    '_RRDD-R',
    '_RCDD-E',
    '_RCDD-R',
    '_RCDD-D',
)

# fit models order
fitmodord = (
    'guw1',
    'guw2',
    'w1',
    'w2',
)

# output stems / [distribution model] / [densitiy]
stmlstfit = [[[] for i in range(len(readst))] for j in range(len(dismodord))]
stmlstmap = [[[] for i in range(len(readst))] for j in range(len(dismodord))]
stmlstanK = [[[] for i in range(len(readst))] for j in range(len(dismodord))]
stmlstang = [[[] for i in range(len(readst))] for j in range(len(dismodord))]
stmlstanG = [[[] for i in range(len(readst))] for j in range(len(dismodord))]

# import directories / [density]
impdirfit = []
impdirmap = []
impdirana = []

# fill lists
for i in range(len(readst)):
    # complete impdir* lists
    dstcsl = '5e'+str(dstexp[i])+"m-2"
    impdirfit.append('../../data/fits_'+dstcsl)
    impdirmap.append('../../data/maps_'+dstcsl)
    impdirana.append('../../data/stats_'+dstcsl)
    del dstcsl
    # complete stmlst* lists
    for stm in os.listdir(impdirfit[i]):
        for dismod in dismodord:
            if dismod in stm:
                stmlstfit[dismodord.index(dismod)][i].append(stm)
    for stm in os.listdir(impdirmap[i]):
        for dismod in dismodord:
            if dismod in stm:
                stmlstmap[dismodord.index(dismod)][i].append(stm)
    for stm in os.listdir(impdirana[i]):
        for dismod in dismodord:
            if dismod in stm:
                if 'KKKK' in stm:
                    stmlstanK[dismodord.index(dismod)][i].append(stm)
                elif 'gggg' in stm:
                    stmlstang[dismodord.index(dismod)][i].append(stm)
                elif 'GaGs' in stm:
                    stmlstanG[dismodord.index(dismod)][i].append(stm)
    del stm, dismod

# distribution model nicknames / [distribution model] / [densitiy]
lstnicnam = [[[] for i in range(len(readst))] for j in range(len(dismodord))]

# fill lstnicnam
for j in range(len(dismodord)):
    for i in range(len(readst)):
        for k in range(len(stmlstfit[j][i])):
            nicnam = dismodord[j][1:]+'-5e'+str(dstexp[i])
            if len(stmlstfit[j][i]) > 1:
                nicnam += '-'+chr(ord('A')+k)
            lstnicnam[j][i].append(nicnam)
del j, i, k, nicnam
