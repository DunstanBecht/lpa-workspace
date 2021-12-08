#!/usr/bin/env python
# coding: utf-8

"""
Perform parallel spatial analyses on the supercomputer.

Submit with:
$ sbatch stats.job
"""

import time
from lpa.input import sets, parallel
import settings

t1 = time.time()
for key in settings.groups:
    for args in settings.groups[key]:
        s = sets.Sample(args['n'], *args['a'], S=args['S']+parallel.rank)
        t2 = time.time()
        parallel.export(s, edgcon='GBB', savtxt=True, expstm=args['s'])
        if parallel.rank == parallel.root:
            print(f"{parallel.size}*{s} ({round((time.time()-t2)/60)}mn)")
if parallel.rank == parallel.root:
    print(f"total time: {round((time.time()-t1)/60)} mn")
