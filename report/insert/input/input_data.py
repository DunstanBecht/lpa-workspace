#!/usr/bin/env python
# coding: utf-8

from lpa.input import data, sets, models

d = sets.Distribution('circle', 400, models.RDD, {'d': 5e13*1e-18}, S=0)

data.export(d, expfmt='txt', expstm='input_data')
