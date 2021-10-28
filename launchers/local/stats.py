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

sizes = { # number of distributions per sample
    5e13: 1000,
    5e14: 100,
    5e15: 10,
}

t1 = time.time()
for i in range(len(settings.densities)):
    n = sizes[settings.densities_m[i]]
    if n > 0:
        for args in settings.arguments(settings.densities[i]):
            s = sets.Sample(n, *args, S=0+parallel.rank)
            t2 = time.time()
            parallel.export(s, edgcon='GBB', savtxt=True)
            if parallel.rank == parallel.root:
                print(f"{parallel.size}*{s} ({round((time.time()-t2)/60)}mn)")
if parallel.rank == parallel.root:
    print(f"total time: {round((time.time()-t1)/60)} mn")