#!/usr/bin/env python
# coding: utf-8

from lpa.input import models, sets, maps

m1 = (models.RDD, {'d': 5e13*1e-18})
m2 = (models.RDD, {'d': 5e13*1e-18})

d1 = sets.Distribution('square', 1000, *m1, S=0, c='PBC1')
d2 = sets.Distribution('square', 1000, *m2, S=0, c='PBC2')

maps.export(d1, expstm='pbc_example_1')
maps.export(d2, expstm='pbc_example_2')
