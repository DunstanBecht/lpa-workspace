#!/usr/bin/env python
# coding: utf-8

"""
Generate input data files.
"""

import os
from datetime import datetime
from lpa.input import sets, data
import settings

datpth = '../../data' # path to the data storage directory

sizes = { # number of distributions per sample for each density
    5e13: 100,
    5e14: 0,
    5e15: 0,
}

rep = 1 # rank of replication

idf = datetime.now().strftime('%Y-%m-%d_%H%M')
cyc = (f"Cycle of generation, simulation and analysis started on "
       f"{datetime.now().strftime('%B %d, %Y at %H:%M')}.\n"
       f"Identifier: {idf}")

for i in range(len(settings.densities)):
    print(f"\n{settings.densities_csl[i]}:")
    cyc += "\n\n"+settings.densities_csl[i]
    dirdat = os.path.join(datpth, f'inputs_{settings.densities_stm[i]}')
    dirnot = os.path.join(datpth, f'notations_{settings.densities_stm[i]}')
    for expdir in (dirdat, dirnot):
        if not os.path.isdir(expdir):
            os.makedirs(expdir)
    for args in settings.arguments(settings.densities[i]):
        n = sizes[settings.densities_m[i]]
        if n > 0:
            s = sets.Sample(sizes[settings.densities_m[i]], *args, S=0)
            ccl = f"{s.d:1.3e}m-2 {s.name('gsmcS')}"
            print(ccl)
            cyc += "\n"+ccl
            data.export(s, expdir=dirdat, pbc=rep)
            stem = s.name(c='stm')
            with open(os.path.join(dirnot, f'{stem}_PBC{rep}.tex'), 'w') as f:
                f.write(s.name(f='nmgsd', c='ttl'))

with open(os.path.join(datpth, 'cycle.txt'), 'w') as f:
    f.write(cyc)
