#!/usr/bin/env python
# coding: utf-8

"""
Script to be launched for the automatic execution of the simulations.
"""

import pysftp
import os
import time

from lpa.xrd import run
from lpa.xrd import code
from lpa.input import notation

from logins import username, password
import settings

path = os.getcwd()

hostname = 'compute-0-1-gpu'

options = { # run options
    5e13: {'f': round(600/11.8), 'r': 4000, 'b': 200},
    5e14: {'f': round(300/3.7), 'r': 2000, 'b': 200},
    5e15: {'f': round(150/2), 'r': 1000, 'b': 200},
}

clndir='xrd'

with pysftp.Connection(hostname, username=username, password=password) as sftp:

    if not os.path.isdir(clndir):
        print('\nClone code.')
        code.clone(clndir)
        time.sleep(5) # wait for tree synchronization

    print('\nMake file.')
    run.make(executer=sftp.execute)

    for i in range(len(settings.densities_m)):
        dstcsl = notation.quantity(settings.densities_m[i], "m-2", 'csl')
        dststm = notation.quantity(settings.densities_m[i], "m-2", 'stm')
        f = str(options[settings.densities_m[i]]['f'])
        r = str(options[settings.densities_m[i]]['r'])
        b = str(options[settings.densities_m[i]]['b'])
        print(f"\n{dstcsl}:", end=" ")
        print(f"Fourier coefficients: {f}", end=", ")
        print(f"block repetitions: {r}", end=", ")
        print(f"block size: {b}")
        impdir = "input_data_"+dststm
        expdir = "output_data_"+dststm
        if impdir in sftp.listdir(path):
            if not expdir in sftp.listdir(path):
                sftp.mkdir(os.path.join(path, expdir))
            for stm in sftp.listdir(os.path.join(path, impdir)):
                t = time.time()
                print(stm, end='')
                cmd, res = run.sample(
                    executer=sftp.execute,
                    impstm=stm,
                    impdir=impdir,
                    expdir=expdir,
                    clndir=clndir,
                    **options[settings.densities_m[i]],
                )
                print(f" ({round((time.time()-t)/60)}mn)")

print("\nFinished")
