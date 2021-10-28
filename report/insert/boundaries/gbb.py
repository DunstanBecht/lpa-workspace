#!/usr/bin/env python
# coding: utf-8

from lpa.input import models, sets, maps

m1 = (models.RDD, {'d': 5e13*1e-18})

d1 = sets.Distribution('square', 1000, *m1, S=0, c='GBB2')

maps.export(d1, expstm='gbb_example_1')
