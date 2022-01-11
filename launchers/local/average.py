#!/usr/bin/env python
# coding: utf-8

"""
Average the simulation outputs files.
"""

import os
from lpa.output import collect
import cycle
import sys

if len(sys.argv)>1:
    cycidf = sys.argv[1]
else:
    cycidf = cycle.select() # cycle identifier
cycdir = cycle.directory(cycidf) # cycle directory
groups = cycle.groups(cycidf, 'outputs') # groups

for group in groups:
    print(f"\n{group}:")
    impdir = os.path.join(cycdir, f'outputs_{group}')
    if os.path.isdir(impdir):
        expdir = os.path.join(cycdir, f'average_{group}')
        if not os.path.isdir(expdir):
            os.makedirs(expdir)
        for stm in os.listdir(impdir):
            print(stm)
            collect.average(
                stm,
                impdir=impdir,
                expdir=expdir,
            )

print("\nAveraging finished.")
