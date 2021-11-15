#!/usr/bin/env python
# coding: utf-8

"""
Generate figures.
"""

from synthesis import *
import matplotlib.pyplot as plt

for appmtd in appmtdord:
    for i in range(len(dismodord)):
        for l in range(len(stmlstfit[i][0])):
            dismod = dismodord[i]
            nicnam = lstnicnam[i][0][l].replace('-5e13', '')
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.1, 3.3))
            fig.subplots_adjust(left=0.26, right=0.96, bottom=0.16, wspace=0.35)
            fig.suptitle(f"{appmtd['nam']} on {nicnam}")
            for j in range(len(fitmodord)):
                for h in [1, 2]:
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
                    lab = f"$ {fitmod.upper()}_{h} $"
                    col = f"C{j}"
                    mkr = '-' if h==1 else ':'
                    ax1.plot(readst, y1, mkr, label=lab, color=col)
                    ax2.plot(readst, y2, mkr, color=col)
            ax1.set_ylabel(fmtfig(appmtd['sym'][0]))
            ax2.set_ylabel(fmtfig(appmtd['sym'][1]))
            fig.legend(loc='center left')
            for ax in (ax1, ax2):
                ax.set_xscale('log')
                ax.set_yscale('log')
                ax.set_xticks(readst)
                ax.set_xticklabels([notation.number(t, c='ttl') for t in readst])
                ax.set_xlabel(fmtfig(r"$ DST \ \left( \mathrm{nm}^{-2} \right) $"))
                ax.grid()
            plt.savefig(f"plots/{appmtd['stm']}-{nicnam}.pdf")

nl = 0
for appmtd in appmtdord:
    with open(f"tex/{appmtd['stm']}-plots.tex", 'w') as f:
        for i in range(len(dismodord)):
            for l in range(len(lstnicnam[i][0])):
                nicnam = lstnicnam[i][0][l].replace('-5e13', '')
                lbl = f"{appmtd['stm']}-{nicnam}"
                stm = f"{appmtd['stm']}-{nicnam}"
                cap = f"{nicnam}"
                f.write(f"\medfig{{{lbl}}}{{load/plots}}{{{stm}}}{{{cap}}}%\n"+nl*"\n")
                nl = (nl+1)%2

input("OK")
