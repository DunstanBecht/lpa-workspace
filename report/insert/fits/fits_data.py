#!/usr/bin/env python
# coding: utf-8

from lpa.output import analyze

stm = 'output_data.dat'

ttl = r"RDD $ \left( d = 5 \times 10^{-4} \mathrm{nm^{-2}} \right) $"

analyze.export(stm, figttl=ttl, fmtfit='pdf')
