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

a = 1.25e13 # lowest density [m^-2]
r = 4 # common ratio (must be a square number)
n = 5 # number of densities generated
k = np.arange(n)
rk = r**k
densities = a*rk # [m^-2]
side_cells_min = np.sqrt(2/densities)*1e9 # for each density [nm]
m = [2**np.arange(5) for k in range(n)]
side_cells = [m[k]*side_cells_min[k] for k in range(n)] # for each density [nm]
side_roi = max([max(side_cells[k]) for k in range(n)]) # roi size [nm]

p = 0.2 # ratio of the area occupied by the cell walls
q = p/(1+np.sqrt(1-p)) # multiplier of cell side for wall thickness

splsiz = 16*rk[::-1] # number of distributions per sample for each density

groups = {}

groups['RRDD-E'] = []
for i in range(n):
    for j in range(len(side_cells[i])):
        prm = {'d': densities[i]*1e-18,
               'v': 'E',
               's': side_cells[i][j]}
        args = {}
        args['n'] = int(splsiz[i])
        args['a'] = ('square', side_roi, models.RRDD, prm)
        args['c'] = 1
        args['S'] = 0
        args['s'] = ("RRDD-E"
                    +'_d'+f"{prm['d']*1e18:1.0f}".zfill(16)+"m-2"
                    +'_s'+f"{prm['s']:1.0f}".zfill(4)+"nm")
        groups['RRDD-E'].append(args)

groups['RCDD-E'] = []
for i in range(n):
    for j in range(len(side_cells[i])):
        prm = {'d': densities[i]*1e-18,
               'v': 'E',
               's': side_cells[i][j],
               't': side_cells[i][j]*q}
        args = {}
        args['n'] = int(splsiz[i])
        args['a'] = ('square', side_roi, models.RCDD, prm)
        args['c'] = 1
        args['S'] = 0
        args['s'] = ("RCDD-E"
                    +'_d'+f"{prm['d']*1e18:1.0f}".zfill(16)+"m-2"
                    +'_s'+f"{prm['s']:1.0f}".zfill(4)+"nm"
                    +'_t'+f"{prm['t']:1.0f}".zfill(4)+"nm")
        groups['RCDD-E'].append(args)

if __name__ == "__main__":
    print("d0 must be of form 2/i**2 with i an integer (to have 2 disl/cell)")
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
