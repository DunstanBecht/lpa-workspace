#!/usr/bin/env python
# coding: utf-8

"""
Fit the models on the simulation outputs.
"""

import os

from lpa.output import analyze
from lpa.input import notation

import settings

print("[OUTPUT FITS]")

for i in range(len(settings.densities_m)):
    density_stm = notation.quantity(settings.densities_m[i], "m-2", 'stm')
    imdir = 'output_data_'+density_stm
    if imdir in os.listdir():
        print("\n"+imdir+":")
        exdir = 'output_fits_'+density_stm
        if not os.path.isdir(exdir):
            os.mkdir(exdir)
        for entry in os.listdir(imdir):
            stm = os.path.splitext(entry)[0]
            if not os.path.isdir(os.path.join(exdir, stm)):
                print(stm)
                not_dir = 'notations_'+density_stm
                ttl_fil = os.path.join(not_dir, stm+'.tex')
                if os.path.isfile(ttl_fil):
                    with open(ttl_fil) as f:
                        title = f.read()
                else:
                    title = None
                analyze.export(
                    stm,
                    imdir=imdir,
                    exdir=exdir,
                    title=title,
                    d=settings.densities[i],
                )

input("\nPress 'enter' to exit...")
