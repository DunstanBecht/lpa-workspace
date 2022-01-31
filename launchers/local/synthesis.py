#!/usr/bin/env python
# coding: utf-8

"""
Synthesizes the results of fits into a single file per harmonic.
"""

import re
import os
import math
import numpy as np
import cycle
import sys

if len(sys.argv)>1:
    cycidf = sys.argv[1]
else:
    cycidf = cycle.select() # cycle identifier
cycdir = cycle.directory(cycidf) # cycle directory
groups = cycle.groups(cycidf, 'fits') # groups

def load(impstm):
    """Load data from fit from a sample."""
    with open(impstm, 'r') as f:
        f.readline()
        dst = eval(f.readline())
        for i in range(4):
            f.readline()
        dat = np.loadtxt(f).T
    if len(dat)==0:
        return None
    res = {
        'j': dat[0],
        'L': dat[1],
        'd': dat[3],
        'R': dat[4],
        'D': dst,
    }
    if len(dat) > 5:
        res['f'] = dat[5]
    return res

def analyze(dat, j):
    """Analyze a model."""
    if dat is None:
        return None
    msk = dat['j']==j
    if not np.any(msk):
        return None
    d = dat['d'][msk]
    R = dat['R'][msk]
    res = {
        'avg-d': np.abs(np.mean(d)*1e18-dat['D'])/dat['D'],
        'avg-R': np.mean(R),
        'std-d': np.std(d)*1e18/dat['D'],
        'std-R': np.std(R),
    }
    if 'f' in dat:
        f = dat['f'][msk]
        res['avg-f'] = np.mean(f)
        res['std-f'] = np.std(f)
    return res

def sample(impstm, j):
    """Analyze a sample."""
    res = {}
    for mod in ('GUW1', 'GUW2', 'W1', 'W2'):
        pth = os.path.join(impstm, f"fits_data_{mod}.dat")
        dat = load(pth)
        res[mod] = analyze(dat, j)
    return res

def adjust(tab):
    """Make the items of a column the same width."""
    for j in range(len(tab[0])):
        w = max([len(tab[i][j]) for i in range(len(tab))])
        for i in range(len(tab)):
            tab[i][j] = format(tab[i][j], f'>{w}')

for group in groups:
    expdir = os.path.join(cycdir, f"synthesis_{group}")
    if not os.path.isdir(expdir):
        os.makedirs(expdir)
    for j in (1, 2):
        lines = {'avg':[], 'std':[]}
        for mtd in lines:
            lines[mtd].append([
                f'distribution',
                f'GUW1-{mtd}-f',
                f'GUW1-{mtd}-d',
                f'GUW2-{mtd}-d',
                f'W1-{mtd}-d',
                f'W2-{mtd}-d',
                f'GUW1-{mtd}-R',
                f'GUW2-{mtd}-R',
                f'W1-{mtd}-R',
                f'W2-{mtd}-R',
                ])
        pth0 = os.path.join(cycdir, f"fits_{group}")
        for smp in os.listdir(pth0):
            pth1 = os.path.join(pth0, smp)
            res = sample(pth1, j)
            for mtd in lines:
                lines[mtd].append([smp]+[
                    f"{res[i0][i1]:12.7e}"
                    if res[i0] is not None else 'N/A'
                    for (i0, i1) in [
                        ('GUW1', f'{mtd}-f'),
                        ('GUW1', f'{mtd}-d'),
                        ('GUW2', f'{mtd}-d'),
                        ('W1',   f'{mtd}-d'),
                        ('W2',   f'{mtd}-d'),
                        ('GUW1', f'{mtd}-R'),
                        ('GUW2', f'{mtd}-R'),
                        ('W1',   f'{mtd}-R'),
                        ('W2',   f'{mtd}-R'),
                    ]
                ])

        for mtd in lines:
            adjust(lines[mtd])
            with open(os.path.join(expdir, f"{mtd}_j{j}.csv"), "w") as f:
                for l in lines[mtd]:
                      f.write("; ".join(l)+"\n")
