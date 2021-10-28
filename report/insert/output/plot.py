#!/usr/bin/env python
# coding: utf-8

from lpa.output import analyze

stm = '100_rho5e13m-2_square_3200nm_RDD_d5e-5nm-2_edge_S0_PBC1_output'

ttl = r"100 RDD $ \left( d = 5 \times 10^{-5} \mathrm{nm^{-2}} \right) $"

dat = analyze.output_data(stm)

analyze.plot(dat, figttl=ttl)

