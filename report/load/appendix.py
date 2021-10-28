#!/usr/bin/env python
# coding: utf-8

"""
Generate LaTex files.
"""

from load import *

# export data.tex
with open('appendix.tex', 'w') as f:
    for j in range(len(dismodord)):
        f.write(r"\subsection{"+dismodord[j][1:]+r"}"+"\n")
        for k in range(len(stmlstfit[j][0])):
            for i in range(len(readst)):
                nicnam = lstnicnam[j][i][k]
                f.write(r"\subsubsection{"+nicnam.replace("_", r"\_")+r"}")
                f.write(r"\label{"+nicnam+r"}"+"\n")
                f.write(r"\res{"+str(dstexp[i])+"}")
                f.write(r"{"+stmlstmap[j][i][k]+"}")
                f.write(r"{"+stmlstfit[j][i][k]+"}")
                f.write(r"{"+stmlstanK[j][i][k]+"}")
                f.write(r"{"+stmlstang[j][i][k]+"}")
                f.write(r"{"+stmlstanG[j][i][k]+"}"+"\n\n")
                
del f, j, i, k

input("OK")
