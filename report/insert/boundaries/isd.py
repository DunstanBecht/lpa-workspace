#!/usr/bin/env python
# coding: utf-8

from lpa.input import models, sets, maps

m1 = (models.RDD, {'d': 1e14*1e-18})
m2 = (models.RCDD, {'v': 'R', 'd': 3e14*1e-18, 's': 200, 't': 10})

d1 = sets.Distribution('circle', 1000, *m1, S=0, c='ISD')
d2 = sets.Distribution('circle', 1000, *m2, S=0, c='ISD')

maps.export(d1, expstm='isd_example_1')
maps.export(d2, expstm='isd_example_2')
