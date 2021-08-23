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
    density_csl = notation.quantity(settings.densities_m[i], "m-2")
    imdir = 'output_data_'+density_csl
    if imdir in os.listdir():
        print("\n"+imdir+":")
        exdir = 'output_fits_'+density_csl
        if not os.path.isdir(exdir):
            os.mkdir(exdir)
        for entry in os.listdir(imdir):
            stm = os.path.splitext(entry)[0]
            if not os.path.isdir(os.path.join(exdir, stm)):
                print(stm)
                not_dir = 'notations_'+density_csl
                with open(os.path.join(not_dir, stm+'.tex')) as f:
                    title = f.read()
                    analyze.export(
                        stm,
                        imdir=imdir,
                        exdir=exdir,
                        title=title,
                        d=settings.densities[i],
                    )

input("\nPress 'enter' to exit...")
