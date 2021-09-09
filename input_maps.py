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
    dstcsl = notation.quantity(settings.densities_m[i], "m-2", 'csl')
    dststm = notation.quantity(settings.densities_m[i], "m-2", 'stm')
    print("\n"+dstcsl+":")
    dirmap = "input_maps_"+dststm
    if not os.path.isdir(dirmap):
        os.mkdir(dirmap)
    for args in settings.arguments(settings.densities[i]):
        d = sets.Distribution(*args, S=0)
        print(d)
        maps.export(d, expdir=dirmap, expfmt='pdf')

input("\nPress 'enter' to exit...")
