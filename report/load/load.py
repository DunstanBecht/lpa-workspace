#!/usr/bin/env python
# coding: utf-8

"""
Load data into lists.
"""

import os
import math
import numpy as np

datpth = '../../data_report' # path to the data storage directory

# order of magnitude of the densities
dstexp = (
    13,
    14,
    15,
)

# real densities [m^-2]
readst = [5*10**exp for exp in dstexp]

# distribution models order
dismodord = (
    '_RRDD-E',
    '_RRDD-R',
    '_RDD',
    '_RCDD-D',
    '_RCDD-E',
    '_RCDD-R',
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
    impdirfit.append(os.path.join(datpth, 'fits_'+dstcsl))
    impdirmap.append(os.path.join(datpth, 'maps_'+dstcsl))
    impdirana.append(os.path.join(datpth, 'stats_'+dstcsl))
    # complete stmlst* lists
    if os.path.isdir(impdirfit[i]):
        for stm in os.listdir(impdirfit[i]):
            for dismod in dismodord:
                if dismod in stm:
                    stmlstfit[dismodord.index(dismod)][i].append(stm)
    else:
        print(f"No fits for density {dstexp[i]}.")
    if os.path.isdir(impdirmap[i]):
        for stm in os.listdir(impdirmap[i]):
            for dismod in dismodord:
                if dismod in stm:
                    stmlstmap[dismodord.index(dismod)][i].append(stm)
    else:
        print(f"No maps for density {dstexp[i]}.")
    if os.path.isdir(impdirana[i]):
        for stm in os.listdir(impdirana[i]):
            for dismod in dismodord:
                if dismod in stm and not 'txt' in stm:
                    if 'KKKK' in stm:
                        stmlstanK[dismodord.index(dismod)][i].append(stm)
                    elif 'gggg' in stm:
                        stmlstang[dismodord.index(dismod)][i].append(stm)
                    elif 'GaGs' in stm:
                        stmlstanG[dismodord.index(dismod)][i].append(stm)
    else:
        print(f"No analyses for density {dstexp[i]}.")

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

# fits data / [fit model] / [distribution model] / [densitiy]
datlstfit = [
                [
                    [
                        []
                    for i in range(len(readst))]
                for j in range(len(dismodord))]
              for e in range(len(fitmodord))
            ]

# fill datlstfit
for e in range(len(fitmodord)):
    for j in range(len(dismodord)):
        for i in range(len(readst)):
            for k in range(len(stmlstfit[j][i])):
                stmdis = stmlstfit[j][i][k]
                fitdat = f'fits_data_{fitmodord[e].upper()}.dat'
                dirpth = os.path.join(impdirfit[i], stmdis, fitdat)
                with open(dirpth, 'r') as f:
                    for l in range(5):
                        f.readline() # skip header
                    datlstfit[e][j][i].append(np.loadtxt(f).T)

# index in fits data
i_j = 0
i_L = 1
i_d = 3
i_r = 4
i_f = 5
