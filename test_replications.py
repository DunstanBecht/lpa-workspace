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
    5e13: 4,
    5e14: 3,
    5e15: 2,
}

if input("\nGenerate input? (y/n) ")=="y":
    for i in range(len(settings.densities_m)):
        density_stm = notation.quantity(settings.densities_m[i], "m-2", 'stm')
        print("\n"+density_stm+":")
        input_dir = "input_data_"+density_stm
        if not os.path.isdir(input_dir):
            os.mkdir(input_dir)
        for r in range(replications[settings.densities_m[i]]+1):
            if r == 0:
                c = None
            else:
                c = 'PBCR'+str(r)
            s = sets.Sample(100,
                'square',
                2000,
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
        density_stm = notation.quantity(settings.densities_m[i], "m-2", 'stm')
        print("\n"+density_stm+":")
        output_dir = "output_data_"+density_stm
        for stm in os.listdir(output_dir):
            if 'test' in stm:
                x, y = collect.load(['L', 'A'], stm, output_dir)
                plt.plot(x, y[0], label=stm)
        plt.legend()
        plt.yscale("log")
        plt.xlabel(r"$L$")
        plt.ylabel(r"$A(L)$")
        plt.show()

input("\nPress 'enter' to exit...")
