#!/usr/bin/env python
# coding: utf-8

"""
This script should be submitted with the command:
sbatch cluster.job
"""

from lpa.input import parallel, analyze, sets, models, notation
from settings import *

fun = ('MMMM', 'KKKK', 'gggg', 'GaGs')

for dis in disord:
    for geo in geoord:
        for edg in geoedgord[geo]:
            siz = geosiz[geo]
            dismod = eval(f'models.{dismodfun[dis]}')
            modprm = dismodprm[dis]
            r = metrad['simulation']
            s = sets.Sample(1000, geo, siz, dismod, modprm, S=parallel.rank)
            worker = analyze.calculate(fun, s, r, ec=edg)
            master = [parallel.average_on_cores(worker[i]) for i in range(len(worker))]
            if parallel.rank == parallel.root:
                for i in range(len(fun)):
                    stm = f"{dismodfun[dis]}{notation.parameters(modprm, c='stm')}_{fun[i]}_{edg}.txt"
                    print(stm)
                    np.savetxt(stm, master[i])
