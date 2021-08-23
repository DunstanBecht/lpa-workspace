#!/usr/bin/env python
# coding: utf-8

"""
Generate input data.
"""

import os

from lpa.input import sets
from lpa.input import data
from lpa.input import notation

import settings

print("[INPUT DATA]")

sizes = { # number of distributions per sample
    5e13: 100,
    5e14: 100,
    5e15: 100,
}

for i in range(len(settings.densities_m)):
    n = sizes[settings.densities_m[i]]
    if n > 0:
        density_csl = notation.quantity(settings.densities_m[i], "m-2", 'csl')
        density_stm = notation.quantity(settings.densities_m[i], "m-2", 'stm')
        print("\n"+density_csl+":")
        exdir_dat = "input_data_"+density_stm
        exdir_not = "notations_"+density_stm
        for exdir in (exdir_dat, exdir_not):
            if not os.path.isdir(exdir):
                os.mkdir(exdir)
        for args in settings.arguments(settings.densities[i]):
            s = sets.Sample(n, *args, S=0)
            print(s)
            data.export(s, exdir=exdir_dat)
            stem = s.name(c='stm')
            with open(os.path.join(exdir_not, stem+".tex"), "w") as f:
                f.write(s.name(f='nmgsd', c='ttl'))

input("\nPress 'enter' to exit...")
