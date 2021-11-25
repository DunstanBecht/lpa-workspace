#!/usr/bin/env python
# coding: utf-8

"""
Run the X-ray diffraction simulations.
"""

import numpy as np
import pysftp
import os
import time
from lpa.xrd import run, code
import settings

options = { # run options
    5e13: {'r': 3125, 'b': 64, 'f': round(60*np.sqrt(100)/(2*np.sqrt(100)))},
    5e14: {'r': 3125, 'b': 64, 'f': round(60*np.sqrt(10)/(2*np.sqrt(10)))},
    5e15: {'r': 3125, 'b': 64, 'f': round(60*np.sqrt(1)/(2*np.sqrt(1)))},
}

if not os.path.isdir('xrd'):
    print("\nClone code.")
    code.clone()

print("\nMake file.")
run.make()
for i in range(len(settings.densities)):
    f = str(options[settings.densities_m[i]]['f'])
    r = str(options[settings.densities_m[i]]['r'])
    b = str(options[settings.densities_m[i]]['b'])
    print(f"\n{settings.densities_csl[i]}:", end=" ")
    print(f"Fourier coefficients: {f}", end=", ")
    print(f"block repetitions: {r}", end=", ")
    print(f"block size: {b}")
    impdir = f'inputs_{settings.densities_stm[i]}'
    expdir = f'outputs_{settings.densities_stm[i]}'
    if impdir in os.listdir():
        if not expdir in os.listdir():
            os.mkdir(expdir)
        for stm in os.listdir(impdir):
            t = time.time()
            print(stm, end='')
            cmd, res = run.sample(
                impstm=stm,
                impdir=impdir,
                expdir=expdir,
                **options[settings.densities_m[i]],
            )
            print(f" ({round((time.time()-t)/60)}mn)")

print("\nFinished")
