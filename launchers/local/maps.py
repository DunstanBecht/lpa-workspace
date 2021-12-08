#!/usr/bin/env python
# coding: utf-8

"""
Generate input maps.
"""

import os
from lpa.input import sets, maps
import settings

datpth = '../../data' # path to the data storage directory

for key in settings.groups:
    print(f"\n{key}:")
    dirmap = os.path.join(datpth, f'maps_{key}')
    if not os.path.isdir(dirmap):
        os.makedirs(dirmap)
    for args in settings.groups[key]:
        d = sets.Distribution(*args['a'], S=args['S'])
        print(d)
        maps.export(d, expdir=dirmap, expfmt='pdf', expstm=args['s'])
