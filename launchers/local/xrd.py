#!/usr/bin/env python
# coding: utf-8

"""
Run the X-ray diffraction simulations.
"""

import numpy as np
import os
import time
from lpa.xrd import run, code

def steps(impdir, impstm):
    """Return the number of Fourier coefficients to generate."""
    pth = os.path.join(impdir, impstm)
    if os.path.isdir(pth):
        pth = os.path.join(pth, os.listdir(pth)[0])
    with open(pth, 'r') as fil:
        fil.readline()
        dst = eval(fil.readline())*1e-18 # [nm^-2]
        for i in range(7):
            fil.readline()
        a3 = eval(fil.readline()) # [nm]
    Lmax = 5/np.sqrt(dst) # [nm]
    return int(Lmax/a3)

wgs = 64 # work-group size
nrp = 200001 # number of work group repetitions

if not os.path.isdir('xrd'):
    print("\nClone code.")
    code.clone()

print("\nMake file.")
run.make()

groups = [e.replace("inputs_", "") for e in os.listdir() if "inputs_" in e]

for group in groups:
    print(f"\n{group}:", end=" ")
    impdir = f'inputs_{group}'
    expdir = f'outputs_{group}'
    if impdir in os.listdir():
        if not expdir in os.listdir():
            os.mkdir(expdir)
        for stm in os.listdir(impdir):
            nfv = steps(impdir, stm)
            t = time.time()
            print(f"{stm} (wgs={wgs} nrp={nrp} nfv={nfv}) ", end='')
            cmd, res = run.sample(
                impstm=stm,
                impdir=impdir,
                expdir=expdir,
                wgs=wgs,
                nrp=nrp,
                nfv=steps(impdir, stm),
            )
            print(f" -> ({round((time.time()-t)/60)}mn)")

print("\nFinished")
