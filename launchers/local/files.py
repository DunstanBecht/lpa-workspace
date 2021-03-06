#!/usr/bin/env python
# coding: utf-8

"""
Generate input data files.
"""

import os
from datetime import datetime
from lpa.input import sets, data
import settings
import cycle

cycidf = cycle.init() # cycle identifier
cycinf = cycle.header(cycidf) # cycle information
cycdir = cycle.directory(cycidf) # cycle directory

for group in settings.groups:
    print(f"\n{group}:")
    cycinf += "\n\n"+group
    dirdat = os.path.join(cycdir, f'inputs_{group}')
    dirnot = os.path.join(cycdir, f'notations_{group}')
    for expdir in (dirdat, dirnot):
        if not os.path.isdir(expdir):
            os.makedirs(expdir)
    for args in settings.groups[group]:
        s = sets.Sample(args['n'], *args['args'], **args['kwargs'])
        ccl = (f"{args['n']:4} * {s.name('gsmcS')} a3={args['a3']:7.2e} "
                  f"PBC{args['pbc']} ({s[0].d*1e18:1.3e}m-2)")
        print(ccl)
        cycinf += "\n"+ccl
        data.export(
            s,
            expdir=dirdat,
            pbc=args['pbc'],
            expstm=args['stm'],
            a3=args['a3'],
        )
        with open(os.path.join(dirnot, f"{args['stm']}.tex"), 'w') as f:
            f.write(s.name(f='nmgsd', c='ttl'))

with open(os.path.join(cycdir, 'cycle-information.txt'), 'w') as f:
    f.write(cycinf)

print("\nInput generation finished.")
