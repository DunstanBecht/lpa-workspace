#!/usr/bin/env python
# coding: utf-8

"""
Generate input maps.
"""

import os
from lpa.input import sets, maps
import settings
import cycle

cycidf = cycle.select() # cycle identifier
cycdir = cycle.directory(cycidf) # cycle directory

for group in settings.groups:
    print(f"\n{group}:")
    dirmap = os.path.join(cycdir, f'maps_{group}')
    if not os.path.isdir(dirmap):
        os.makedirs(dirmap)
    for args in settings.groups[group]:
        d = sets.Distribution(*args['a'], S=args['S'])
        print(d)
        maps.export(
            d,
            expdir=dirmap,
            expfmt='pdf',
            expstm=args['s'],
        )

print("\nMaps generation finished.")
