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

idf = datetime.now().strftime('%Y-%m-%d_%H%M')
cyc = (f"Cycle of generation, simulation and analysis started on "
       f"{datetime.now().strftime('%B %d, %Y at %H:%M')}.\n"
       f"Identifier: {idf}\n"
       f"The distribution models below are studied.")

for key in settings.groups:
    print(f"\n{key}:")
    cyc += "\n\n"+key
    dirdat = os.path.join(datpth, f'inputs_{key}')
    dirnot = os.path.join(datpth, f'notations_{key}')
    for expdir in (dirdat, dirnot):
        if not os.path.isdir(expdir):
            os.makedirs(expdir)
    for args in settings.groups[key]:
        s = sets.Sample(args['n'], *args['a'], S=args['S'])
        ccl = f"{args['n']:4} * {s.name('gsmcS')} PBC{args['c']} ({s[0].d*1e18:1.3e}m-2)"
        print(ccl)
        cyc += "\n"+ccl
        data.export(s, expdir=dirdat, pbc=args['c'], expstm=args['s'])
        with open(os.path.join(dirnot, f"{args['s']}.tex"), 'w') as f:
            f.write(s.name(f='nmgsd', c='ttl'))

with open(os.path.join(datpth, 'cycle-information.txt'), 'w') as f:
    f.write(cyc)
