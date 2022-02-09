#!/usr/bin/env python
# coding: utf-8

"""
This script generates some LaTeX tables about the ranges of the filters.
"""

import os
import numpy as np

def M_filter(path, f_match):
    col = {'F1':-2, 'F2':-1}
    with open(path, 'r') as f:
        cnt = f.readlines()
        val = eval(cnt[-2].split(',')[col[f_match]])
        std = eval(cnt[-1].split(',')[col[f_match]])
    return [val, std]

def M_j(stm):
    return [eval(stm[1:9]), eval(stm[11])]

def data(group, f_match, j_match):
    tab = []
    impdir = f"../../cycle_final/filters_{group}"
    for fil in os.listdir(impdir):
        M, j = M_j(fil)
        if j == j_match:
            tup = M_filter(os.path.join(impdir, fil), f_match)
            tab.append([M]+tup)
    tab.sort(key =lambda x: x[0])
    return np.array(tab)

def tab(group, f_match, j_list=[1,2]):
    dat = []
    for j in j_list:
        dat.append(data(group, f_match, j))
    M_list = dat[0].T[0]
    col = r">{\centering\arraybackslash}X|"
    tex = r"\begin{tabularx}{\linewidth}{|c|"+col*len(M_list)+"}"+"\n"
    tex += r"\hline"+"\n"
    tex += r"\diagbox{\gls{hmc}}{\( s \sqrt{\gls{dst}} \)} & "
    tex += fr"{' & '.join([str(M) for M in M_list])} \\"+"\n"
    tex += r"\hline"+"\n"
    for i in range(len(j_list)):
        tex += fr"{j_list[i]}"
        for k in range(len(M_list)):
            tex += fr" & \( {dat[i][k][1]:1.1f} \pm {dat[i][k][2]:1.2f} \)"
        tex += r" \\"+"\n"+r"\hline"+"\n"
    tex += "\end{tabularx}"+"\n"
    return tex

for group in ['RRDD-E_virtual', 'RCDD-E_virtual']:
    for flt in ['F1', 'F2']:
        with open(f"tex/{group}_{flt}.tex", 'w') as f:
            f.write(tab(group, flt))
