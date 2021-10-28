#!/usr/bin/env python
# coding: utf-8

from lpa.input import models, sets, maps

m1 = (models.RRDD, {'v': 'E', 's': 200, 'f': 2})
m2 = (models.RRDD, {'v': 'R', 's': 400, 'f': 8})

d1 = sets.Distribution('circle', 1000, *m1, S=0)
d2 = sets.Distribution('square', 2000, *m2, S=0)

maps.export(d1, expstm='rrdd_example_1')
maps.export(d2, expstm='rrdd_example_2')
