#!/usr/bin/env python
# coding: utf-8

"""
Script to be launched for the automatic execution of the simulations.
"""

import pysftp
import os

from lpa.xrd import run
from lpa.input import notation

from logins import username, password
import settings

path = os.getcwd()

hostname = 'compute-0-1-gpu'

options = { # run options
    5e13: {'f': round(600/11.8), 'r': 4000},
    5e14: {'f': round(300/3.7), 'r': 2000},
    5e15: {'f': round(150/2), 'r': 1000},
}

with pysftp.Connection(hostname, username=username, password=password) as sftp:

    print('\nMake file.')
    run.make(executer=sftp.execute)

    for i in range(len(settings.densities_m)):
        density_csl = notation.quantity(settings.densities_m[i], "m-2", 'csl')
        density_stm = notation.quantity(settings.densities_m[i], "m-2", 'stm')
        print("\n"+density_csl+":")
        imdir = "input_data_"+density_stm
        exdir = "output_data_"+density_stm
        if imdir in sftp.listdir(path):
            if not exdir in sftp.listdir(path):
                sftp.mkdir(os.path.join(path, exdir))
            for stm in sftp.listdir(os.path.join(path, imdir)):
                run.run(
                    imstm=stm,
                    executer=sftp.execute,
                    imdir=imdir,
                    exdir=exdir,
                    **options[settings.densities_m[i]],
                )

print("\nFinished")
