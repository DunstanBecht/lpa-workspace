#!/usr/bin/env python
# coding: utf-8

import os
import matplotlib.pyplot as plt
import simulation
import expression
from lpa.input import notation
from settings import *

for dis in disord:
    for geo in geoord:
        for edg in geoedgord[geo]:
            for fun in funord:
                for sub in funord[fun][1]:
                    for met in metord:
                        siz = geosiz[geo]
                        modfun = dismodfun[dis]
                        modprm = dismodprm[dis]
                        rad = metrad[met]
                        mrk = metmrk[met]
                        res = eval(met+'.'+modfun)(rad, geo, siz, edg, modprm)
                        i = funord[fun][0]
                        j = funord[fun][1][sub]
                        col = f"C{j}"
                        lab = f"$\mathrm{{{fun}}}^{{{edg}}}_{{{sub}}}$ {met}"
                        plt.plot(rad, res[i][j], mrk, label=lab, color=col)
                plt.title(f"{modfun}{notation.parameters(modprm, c='ttl')} {geo} {siz}nm")
                plt.xlabel(r"$r$ (nm)")
                plt.legend()
                plt.grid()
                subs = '_'.join([fun+sub for sub in funord[fun][1]])
                filnam = f"{'_'.join((subs, edg, dis, geo))}.pdf"
                print(filnam)
                plt.savefig(f"../plots/{filnam}")
                plt.clf()
