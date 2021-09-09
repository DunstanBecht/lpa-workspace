#!/usr/bin/env python
# coding: utf-8

"""
Script to determine the optimal number of replications for each density.
"""

import os
import matplotlib.pyplot as plt

from lpa.input import sets
from lpa.input import data
from lpa.input import notation
from lpa.input import models
from lpa.output import collect

import settings

replications = { # maximum number of replications tested
    5e13: 3,
    5e14: 2,
    5e15: 1,
}

if input("\nGenerate input? (y/n) ")=="y":
    for i in range(len(settings.densities_m)):
        dststm = notation.quantity(settings.densities_m[i], "m-2", 'stm')
        print("\n"+dststm+":")
        input_dir = "input_data_"+dststm
        if not os.path.isdir(input_dir):
            os.mkdir(input_dir)
        for r in range(replications[settings.densities_m[i]]+1):
            if r == 0:
                c = None
            else:
                c = 'PBCR'+str(r)
            s = sets.Sample(100,
                'square',
                4000,
                models.RDD,
                {'d': settings.densities[i]},
                'edge',
                c,
                S=0,
            )
            print(s)
            data.export(
                s,
                exdir=input_dir,
                exstm='test_'+s.name(c='stm', f='dc'),
            )

if input("\nPlot outputs (y/n) ")=="y":
    for i in range(len(settings.densities_m)):
        dststm = notation.quantity(settings.densities_m[i], "m-2", 'stm')
        print("\n"+dststm+":")
        outdir = "output_data_"+dststm
        for stm in os.listdir(outdir):
            if 'test' in stm:
                x, y = collect.load(['L', 'A'], stm, outdir)
                plt.plot(x, y[0], label=stm)
        plt.legend()
        plt.yscale("log")
        plt.xlabel(r"$L$")
        plt.ylabel(r"$A(L)$")
        plt.show()

input("\nPress 'enter' to exit...")
