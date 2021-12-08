#!/usr/bin/env python
# coding: utf-8

"""
Fit the models on the simulation outputs.
"""

import numpy as np
import os
from lpa.output import analyze

datpth = '../../data' # path to the data storage directory

groups = [e.replace("outputs_", "") for e in os.listdir(datpth) if "outputs_" in e]

for key in groups:
    print(f"\n{key}:")
    impdir = os.path.join(datpth, f'outputs_{key}')
    notdir = f'notations_{key}'
    if os.path.isdir(impdir):
        expdir = os.path.join(datpth, f'fits_{key}')
        if not os.path.isdir(expdir):
            os.makedirs(expdir)
        for entry in os.listdir(impdir):
            stm = os.path.splitext(entry)[0]
            if not os.path.isdir(os.path.join(expdir, f"{stm}_analysis")):
                print(stm)
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
