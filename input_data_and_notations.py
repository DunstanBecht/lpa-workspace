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
        dstcsl = notation.quantity(settings.densities_m[i], "m-2", 'csl')
        dststm = notation.quantity(settings.densities_m[i], "m-2", 'stm')
        print(f"\n{dstcsl}:")
        dirdat = "input_data_"+dststm
        dirnot = "notations_"+dststm
        for expdir in (dirdat, dirnot):
            if not os.path.isdir(expdir):
                os.mkdir(expdir)
        for args in settings.arguments(settings.densities[i]):
            s = sets.Sample(n, *args, S=0)
            print(f"{s.d:1.3e}m-2 {s.name('gsmcS')}")
            data.export(s, expdir=dirdat, pbc=1)
            stem = s.name(c='stm')
            with open(os.path.join(dirnot, stem+".tex"), "w") as f:
                f.write(s.name(f='nmgsd', c='ttl'))

input("\nPress 'enter' to exit...")
