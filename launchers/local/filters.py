#!/usr/bin/env python
# coding: utf-8

"""
Determine the range of the filters for RRDD and RCDD distributions.
"""

import os
from lpa.output import analyze
import cycle
import sys
import numpy as np

j_list = [1, 2]

if len(sys.argv)>1:
    cycidf = sys.argv[1]
else:
    cycidf = cycle.select() # cycle identifier
cycdir = cycle.directory(cycidf) # cycle directory
groups = cycle.groups(cycidf, 'average') # groups

def stm_M_L1_L2_M1_M2_j(j, dat):
    stm = dat['stm']
    s = eval(dat['stm'].split('_s_')[1].split('_nm_')[0])
    d = dat['d']
    M = s*np.sqrt(d)
    i = dat['index'][j]
    L_F1 = dat['L'][dat['F1'][i]-1]
    L_F2 = dat['L'][dat['F2'][i]-1]
    M_F1 = L_F1*np.sqrt(d)
    M_F2 = L_F2*np.sqrt(d)
    return dat['stm'], M, L_F1, L_F2, M_F1, M_F2, j

for group in groups:
    impdir = os.path.join(cycdir, f'average_{group}')
    if os.path.isdir(impdir):
        expdir = os.path.join(cycdir, f'filters_{group}')
        if not os.path.isdir(expdir):
            os.makedirs(expdir)
        M_list = []
        table = []
        for stm in os.listdir(impdir):
            dat = analyze.output_data(stm, impdir=impdir)
            for j in j_list:
                table.append(stm_M_L1_L2_M1_M2_j(j, dat))
            if not table[-1][1] in M_list:
                M_list.append(table[-1][1])
        w = max([len(tup[0]) for tup in table])
        for M in M_list:
            for j in j_list:
                M_F1_sum = []
                M_F2_sum = []
                filnam = f"M{M:1.1e}_j{j}.txt".replace('+', '')
                with open(os.path.join(expdir, filnam), 'w') as f:
                    f.write((f"{format('distribution', f'>{w}')},"
                             f"{'L_F1 [nm]':>10},{'L_F2 [nm]':>10},"
                             f"{'M_F1 [1]':>10},{'M_F2 [1]':>10}\n"))
                    for tup in table:
                        if tup[1]== M and tup[-1]==j:
                            f.write((f"{tup[0]},"
                                     f"{tup[2]:10.2f},{tup[3]:10.2f},"
                                     f"{tup[4]:10.2f},{tup[5]:10.2f}\n"))
                            M_F1_sum.append(tup[4])
                            M_F2_sum.append(tup[5])
                    M_F1_avg = sum(M_F1_sum)/len(M_F1_sum)
                    M_F2_avg = sum(M_F2_sum)/len(M_F2_sum)
                    M_F1_std = np.std(M_F1_sum)
                    M_F2_std = np.std(M_F2_sum)
                    f.write((f"{format('average', f'>{w}')},"
                                 f"{'None':>10},{'None':>10},"
                                 f"{M_F1_avg:10.2f},{M_F2_avg:10.2f}\n"))
                    f.write((f"{format('standard deviation', f'>{w}')},"
                                 f"{'None':>10},{'None':>10},"
                                 f"{M_F1_std:10.2f},{M_F2_std:10.2f}\n"))

print("Filter ranges evaluation finished.")
