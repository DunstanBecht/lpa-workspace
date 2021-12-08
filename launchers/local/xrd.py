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

r = 3125
b = 64
f = 100

if not os.path.isdir('xrd'):
    print("\nClone code.")
    code.clone()

print("\nMake file.")
run.make()

groups = [e.replace("inputs_", "") for e in os.listdir() if "inputs_" in e]

for key in groups:
    print(f"\n{key}:", end=" ")
    print(f"Fourier coefficients: {f}", end=", ")
    print(f"block repetitions: {r}", end=", ")
    print(f"block size: {b}")
    impdir = f'inputs_{key}'
    expdir = f'outputs_{key}'
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
                r=r,
                b=b,
                f=f,
            )
            print(f" ({round((time.time()-t)/60)}mn)")

print("\nFinished")
