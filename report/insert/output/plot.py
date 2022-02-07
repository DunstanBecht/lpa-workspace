#!/usr/bin/env python
# coding: utf-8

from lpa.output import analyze

stm = 'output_data.dat'

ttl = r"RDD $ \left( d = 5 \times 10^{-5} \mathrm{nm^{-2}} \right) $"

dat = analyze.output_data(stm)

analyze.plot(dat, figttl=ttl)
