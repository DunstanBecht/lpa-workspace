#!/usr/bin/env python
# coding: utf-8

"""
Generate figures.
"""

from synthesis import *
import matplotlib.pyplot as plt

for i in range(len(dismodord)):
    for l in range(len(stmlstfit[i][0])):
        dismod = dismodord[i]
        nicnam = lstnicnam[i][0][l].replace('-5e13', '')
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))
        fig.subplots_adjust(left=0.31, right=0.96, bottom=0.15, wspace=0.33)
        fig.suptitle(f"Relative density deviation as a function of $ L_{{MAX}} $ in GUW1")
        j = 0 # guw 1
        for k in range(len(readst)):
            for h in [1, 2]:
                dst = readst[k]
                fittbl = datlstfit[j][i][k][l]
                mashmc = fittbl[i_j]==h
                fittbl = fittbl.T[mashmc].T
                y1 = []
                y2 = []
                for m in range(0, len(fittbl[i_L])):
                    
                    y = appmtdord[0]['fun'](dst, fittbl.T[:1+m].T)
                    y1.append(y[0])
                    y = appmtdord[1]['fun'](dst, fittbl.T[:1+m].T)
                    y2.append(y[0])

                lab = fmtfig(f"$ j = {h} $, {notation.quantity(readst[k], 'm^{-2}', c='ttl')}")
                col = f"C{k}"
                mkr = '-' if h==1 else ':'

                fittbl2 = datlstfit[1][i][k][l]
                mashmc = fittbl2[i_j]==h
                fittbl2 = fittbl2.T[mashmc].T
                
                L_f2 = fittbl2[i_L][-1]
                print(dismod, dst, L_f2)
                ax1.plot(fittbl[i_L]/L_f2, y1, mkr, label=lab, color=col)
                ax2.plot(fittbl[i_L]/L_f2, y2, mkr, color=col)
        ax1.set_ylabel(fmtfig(appmtdord[0]['sym'][0]))
        ax2.set_ylabel(fmtfig(appmtdord[1]['sym'][0]))
        fig.legend(loc='center left')
        for ax in (ax1, ax2):
            ax.set_xscale('log')
            #ax.set_yscale('log')
            ax.set_xlabel(r"$ L_{{MAX}}/{L_{MAX}}^{MAX, j, GUW2} $")
            ax.grid()
        plt.savefig(f"plots/GUW1-{nicnam}.pdf")

nl = 0
for appmtd in appmtdord:
    with open(f"tex/guw1-plots.tex", 'w') as f:
        for i in range(len(dismodord)):
            for l in range(len(lstnicnam[i][0])):
                nicnam = lstnicnam[i][0][l].replace('-5e13', '')
                lbl = f"guw1-{nicnam}"
                stm = f"guw1-{nicnam}"
                cap = f"{nicnam}"
                f.write(f"\medfig{{{lbl}}}{{load/plots}}{{{stm}}}{{{cap}}}%\n"+nl*"\n")
                nl = (nl+1)%2

input("OK")
