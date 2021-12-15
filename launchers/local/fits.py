#!/usr/bin/env python
# coding: utf-8

"""
Fit the models on the simulation outputs.
"""

import numpy as np
import os
from lpa.output import analyze
import cycle

cycidf = cycle.select() # cycle identifier
cycdir = cycle.directory(cycidf) # cycle directory
groups = cycle.groups(cycidf, 'outputs') # groups

for group in groups:
    print(f"\n{group}:")
    impdir = os.path.join(cycdir, f'outputs_{group}')
    notdir = f'notations_{group}'
    if os.path.isdir(impdir):
        expdir = os.path.join(cycdir, f'fits_{group}')
        if not os.path.isdir(expdir):
            os.makedirs(expdir)
        for entry in os.listdir(impdir):
            stm = os.path.splitext(entry)[0]
            if not os.path.isdir(os.path.join(expdir, f"{stm}_analysis")):
                print(stm)
                ttlfil = f"{stm.replace('_output', '')}.tex"
                ttlpth = os.path.join(cycdir, notdir, ttlfil)
                if os.path.isfile(ttlpth):
                    with open(ttlpth) as f:
                        figttl = f.read()
                else:
                    figttl = stm
                analyze.export(
                    stm,
                    impdir=impdir,
                    expdir=expdir,
                    figttl=figttl,
                    frrprt=np.real, # np.real (default) | np.absolute
                )
