#!/usr/bin/env python
# coding: utf-8

"""
This script should be submitted on a supercomputer with the command:
$ sbatch analysis_parallel.job
"""

from lpa.input import  models, sets, parallel
import warnings

m = (models.RDD, {'d': 5e13*1e-18})

s = sets.Sample(2000, 'square', 3200, *m, S=parallel.rank)

warnings.filterwarnings("ignore")

parallel.export(s, expstm='example', edgcon='GBB')
