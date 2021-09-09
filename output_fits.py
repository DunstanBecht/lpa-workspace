#!/usr/bin/env python
# coding: utf-8

"""
Fit the models on the simulation outputs.
"""

import os
import numpy as np

from lpa.output import analyze
from lpa.input import notation

import settings

print("[OUTPUT FITS]")

for i in range(len(settings.densities_m)):
    dststm = notation.quantity(settings.densities_m[i], "m-2", 'stm')
    impdir = 'output_data_'+dststm
    if impdir in os.listdir():
        print("\n"+impdir+":")
        expdir = 'output_fits_'+dststm
        if not os.path.isdir(expdir):
            os.mkdir(expdir)
        for entry in os.listdir(impdir):
            stm = os.path.splitext(entry)[0]
            if not os.path.isdir(os.path.join(expdir, stm)):
                print(stm)
                notdir = 'notations_'+dststm
                ttlfil = os.path.join(notdir, stm+'.tex')
                if os.path.isfile(ttlfil):
                    with open(ttlfil) as f:
                        title = f.read()
                else:
                    title = stm
                analyze.export(
                    stm,
                    impdir=impdir,
                    expdir=expdir,
                    title=title,
                    d=settings.densities[i],
                    j=np.array([1, 2]),
                )

input("\nPress 'enter' to exit...")
