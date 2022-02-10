#!/usr/bin/env python
# coding: utf-8

"""
The studied densities must be extracted from a geometric sequence with 'a'
(scale factor) the lowest density and 'r' (common ratio) a square number.
If the common ratio 'r' is of the form 'k**2' then the sizes of the cells
containing a fixed number 'n' of dislocations follow an arithmetic sequence
with a common difference of 'k'. This makes it possible to choose the size
of the crystal which must be a multiple of the LCM of these cell sizes.
Whenever possible, densities with the least number of zeros in scientific
notation should be chosen.
"""

import numpy as np
from lpa.input import models

# general parameters ------------------------------------------------------ #

a = 1.25e13 # lowest density [m^-2]
r = 4 # common ratio (must be a square number) to obtain higher densities
n = 6 # number of studied densities
rk = r**np.arange(n) # multiplicative coefficients of a
densities = a*rk # list of the studied densities [m^-2]
side_cells_min = np.sqrt(2/densities)*1e9 # lower s parameters [nm]
m = [2**np.arange(5) for k in range(n)] # multiplicative coefficients of s
side_cells = [m[k]*side_cells_min[k] for k in range(n)] # s parameters [nm]
side_roi = max([max(side_cells[k]) for k in range(n)]) # ROI sizes [nm]
p = 0.2 # ratio of the area occupied by the cell walls
q = p/(1+np.sqrt(1-p)) # multiplier of cell side for wall thickness

# a3 parameter(s) for each density ---------------------------------------- #

if False: # only for asymptotic behavior
    # don't forget to reduce the number of steps in xrd.py
    m = [2**np.arange(1) for k in range(n)] # multiplicative coefficients of a3
    step_min = 2**np.arange(n)[::-1]*0.5 # minimum a3 values [nm]
    step = [m[k]*step_min[k] for k in range(n)]
elif False: # vary a3 as a function of density
    m = [2**np.arange(3) for k in range(n)] # multiplicative coefficients of a3
    step_min = 2**np.arange(n)[::-1]*1 # minimum a3 values [nm]
    step = [m[k]*step_min[k] for k in range(n)]
else: # take the same a3 for all densities
    step = [[1.5] for k in range(n)]

# number of distributions per sample for each density --------------------- #

if False: # vary the number of files generated as a function of density
    splsiz = r*rk[::-1]
else: # take the same number of file for every density
    splsiz = 4*np.ones(n)

# groups generation ------------------------------------------------------- #

groups = {}

for variant in [
    #'E',
    #'R',
]:
    groups[f"RRDD-{variant}"] = []
    for i in range(n):
        for j in range(len(side_cells[i])):
            for k in range(len(step[i])):
                prm = {'d': densities[i]*1e-18,
                       'v': variant,
                       's': side_cells[i][j]}
                args = {}
                args['n'] = int(splsiz[i])
                args['args'] = ('square', side_roi, models.RRDD, prm)
                args['pbc'] = 1
                args['kwargs'] = {'S': 0}
                args['a3'] = step[i][k]
                args['stm'] = (f"RRDD-{variant}"
                               +'_a3_'+f"{args['a3']:1.2e}_nm"
                               +'_d_'+f"{prm['d']*1e18:1.2e}_m-2"
                               +'_s_'+f"{prm['s']:1.2e}_nm").replace('+', '')
                print(args['stm'])
                groups[f"RRDD-{variant}"].append(args)

for variant in [
    #'E',
    #'R',
]:
    groups[f"RCDD-{variant}"] = []
    for i in range(n):
        for j in range(len(side_cells[i])):
            for k in range(len(step[i])):
                prm = {'d': densities[i]*1e-18,
                       'v': variant,
                       's': side_cells[i][j],
                       't': side_cells[i][j]*q}
                args = {}
                args['n'] = int(splsiz[i])
                args['args'] = ('square', side_roi, models.RCDD, prm)
                args['pbc'] = 1
                args['kwargs'] = {'S': 0}
                args['a3'] = step[i][k]
                args['stm'] = (f"RCDD-{variant}"
                               +'_a3_'+f"{args['a3']:1.2e}_nm"
                               +'_d_'+f"{prm['d']*1e18:1.2e}_m-2"
                               +'_s_'+f"{prm['s']:1.2e}_nm"
                               +'_t_'+f"{prm['t']:1.7e}_nm").replace('+', '')
                print(args['stm'])
                groups[f"RCDD-{variant}"].append(args)

if True:
    groups[f"RDD"] = []
    for i in range(n):
        for k in range(len(step[i])):
            prm = {'d': densities[i]*1e-18}
            args = {}
            args['n'] = int(splsiz[i])
            args['args'] = ('circle', 3600, models.RDD, prm)
            args['pbc'] = 0
            args['kwargs'] = {'S': 0, 'c': 'ISD'}
            args['a3'] = step[i][k]
            args['stm'] = (f"RDD"
                           +'_a3_'+f"{args['a3']:1.2e}_nm"
                           +'_d_'+f"{prm['d']*1e18:1.2e}_m-2").replace('+', '')
            print(args['stm'])
            groups[f"RDD"].append(args)

if __name__ == "__main__":
    print("\nd0 must be of form 2/i**2 with i an integer (to have 2 disl/cell)")
    a_candidates = []
    for i in range(1, 1000):
        d0 = (2/i**2)*1e18 # [m^-2]
        d0str = f"{d0:1.0f}"
        if len(d0str.strip("0"))<=3: # limit the number of decimal places
            print(f"\nWith i = {i} -> d0 = {d0:1e}m^-2:")
            d = d0*rk # [m^-2]
            s_min = np.sqrt(2/d)*1e9 # [nm]
            for k in range(n):
                print(f"d{k} = {d[k]:10.10e}m^-2", end=" ")
                print(f"s{k}_min = {s_min[k]:15.10f} nm", end="")
                if int(s_min[k]) == s_min[k]:
                    print("")
                else:
                    print(r" (!)")
