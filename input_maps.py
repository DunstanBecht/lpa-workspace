#!/usr/bin/env python
# coding: utf-8

"""
Generate distribution maps.
"""

import os

from lpa.input import sets
from lpa.input import maps
from lpa.input import notation

import settings

print("[INPUT MAPS]")

for i in range(len(settings.densities_m)):
    density_csl = notation.quantity(settings.densities_m[i], "m-2", 'csl')
    density_stm = notation.quantity(settings.densities_m[i], "m-2", 'stm')
    print("\n"+density_csl+":")
    exdir = "input_maps_"+density_stm
    if not os.path.isdir(exdir):
        os.mkdir(exdir)
    for args in settings.arguments(settings.densities[i]):
        d = sets.Distribution(*args, S=0)
        print(d)
        maps.export(d, exdir=exdir, exfmt='pdf')

input("\nPress 'enter' to exit...")
