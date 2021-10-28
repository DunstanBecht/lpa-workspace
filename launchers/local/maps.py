#!/usr/bin/env python
# coding: utf-8

"""
Generate input maps.
"""

import os
from lpa.input import sets, maps
import settings

datpth = '../../data' # path to the data storage directory

for i in range(len(settings.densities)):
    print(f"\n{settings.densities_csl[i]}:")
    dirmap = os.path.join(datpth, f'maps_{settings.densities_stm[i]}')
    if not os.path.isdir(dirmap):
        os.makedirs(dirmap)
    for args in settings.arguments(settings.densities[i]):
        d = sets.Distribution(*args, S=0)
        print(d)
        maps.export(d, expdir=dirmap, expfmt='pdf')
