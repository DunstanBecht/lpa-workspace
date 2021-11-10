#!/usr/bin/env python
# coding: utf-8

"""
Generate figures.
"""

from synthesis import *
import matplotlib.pyplot as plt

for h in [1, 2]:
    for appmtd in appmtdord:
        for i in range(len(dismodord)):
            for l in range(len(stmlstfit[i][0])):
                dismod = dismodord[i]
                nicnam = lstnicnam[i][0][l].replace('-5e13', '')
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
                fig.subplots_adjust(left=0.1, right=0.96, bottom=0.1)
                fig.suptitle(f"{appmtd['nam']} for $ j = {h} $ on {nicnam}")
                for j in range(len(fitmodord)):
                    y1 = []
                    y2 = []
                    for k in range(len(readst)):
                        stmdis = stmlstfit[i][k][l]
                        fitmod = fitmodord[j]
                        dst = readst[k]
                        fittbl = datlstfit[j][i][k][l]
                        mashmc = fittbl[i_j]==h
                        fittbl = fittbl.T[mashmc].T
                        y = appmtd['fun'](dst, fittbl)
                        y1.append(y[0])
                        y2.append(y[1])
                    ax1.plot(readst, y1, label=f"$ {fitmod.upper()}_{h} $")
                    ax2.plot(readst, y2, label=f"$ {fitmod.upper()}_{h} $")
                ax1.set_ylabel(fmtfig(appmtd['sym'][0]))
                ax2.set_ylabel(fmtfig(appmtd['sym'][1]))
                for ax in (ax1, ax2):
                    ax.set_xscale('log')
                    ax.set_xticks(readst)
                    ax.set_xticklabels([notation.number(t, c='ttl') for t in readst])
                    ax.set_xlabel(r"real density $ \left( \mathrm{nm}^{-2} \right) $")
                    ax.grid()
                    ax.legend()
                plt.savefig(f"plots/{appmtd['stm']}-{nicnam}-j{h}.pdf")

input("OK")
