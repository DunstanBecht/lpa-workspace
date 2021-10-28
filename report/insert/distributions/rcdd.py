#!/usr/bin/env python
# coding: utf-8

from lpa.input import models, sets, maps

m1 = (models.RCDD, {'v': 'R', 'd': 1e14*1e-18, 's': 200, 't': 20})
m2 = (models.RCDD, {'v': 'D', 'd': 5e13*1e-18, 's': 400, 't': 20, 'l': 50})

d1 = sets.Distribution('circle', 1000, *m1, S=0)
d2 = sets.Distribution('square', 2000, *m2, S=1)

maps.export(d1, expstm='rcdd_example_1')
maps.export(d2, expstm='rcdd_example_2')
