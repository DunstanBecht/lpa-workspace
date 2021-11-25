#!/usr/bin/env python
# coding: utf-8

"""
Fit the models on the simulation outputs.
"""

import numpy as np
import os
from lpa.output import analyze
import settings

datpth = '../../data' # path to the data storage directory

for i in range(len(settings.densities)):
    print(f"\n{settings.densities_csl[i]}:")
    impdir = os.path.join(datpth, f'outputs_{settings.densities_stm[i]}')
    if os.path.isdir(impdir):
        expdir = os.path.join(datpth, f'fits_{settings.densities_stm[i]}')
        if not os.path.isdir(expdir):
            os.makedirs(expdir)
        for entry in os.listdir(impdir):
            stm = os.path.splitext(entry)[0]
            if not os.path.isdir(os.path.join(expdir, f"{stm}_analysis")):
                print(stm)
                notdir = f'notations_{settings.densities_stm[i]}'
                ttlfil = f"{stm.replace('_output', '')}.tex"
                ttlpth = os.path.join(datpth, notdir, ttlfil)
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
