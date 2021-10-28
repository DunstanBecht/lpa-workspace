#!/usr/bin/env python
# coding: utf-8

from lpa.input import models, sets, analyze

m = (models.RDD, {'d': 5e13*1e-18})

s = sets.Sample(200000, 'square', 3200, *m, S=0)

analyze.export(s, expstm='example', edgcon='GBB')
