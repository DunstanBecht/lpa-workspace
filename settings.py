#!/usr/bin/env python
# coding: utf-8

"""
Default parameter values.
"""

import copy
import numpy as np
import math
import fractions

from lpa.input import models
from lpa.input import notation

densities_m = [5e13, 5e14, 5e15] # studied dislocation densities [m^-2]

densities = [d*1e-18 for d in densities_m] # [nm^-2]

def arguments(
    d: float,
    s: int = 3200,
    b: str = 'PBCR1',
    c: int = (200, 400),
    p: float = 0.2,
    k: tuple = (0.25, 0.5, 1, 2.5, 5),
    ) -> list:
    """
    Return a list of tuples containing the instantiation arguments.

    Input:
        d: dislocation density [nm^-2]
        s: side of the region of interest [nm] (RDD, RRDD-*)
        b: boundary conditions
        c: sides of the subareas [nm] (RRDD-*)
        p: ratio of the area occupied by the cell walls (RCDD-*)
        k: multiplier of the inter-dislocation distance for dipole length

    Output:
        t: tuples containing the instantiation arguments
    """
    for subarea in c:
        if s%subarea != 0:
            raise ValueError("incorret subarea side: "+str(subarea)+" nm")
    i = 1/np.sqrt(d) # inter dislocation distance [nm]
    # parameters for RCDD-*
    q = (1+np.sqrt(1-p))/p # multiplier of wall thickness for cell side
    # parameters for RCDD-E and RCDD-R
    t1 = i # thickness of the cell walls [nm]
    c1 = t1*q # cell sides [nm]
    s1 = max(round(s/c1), 1)*c1 # shape side [nm]
    # parameters for RCDD-D
    frac = [fractions.Fraction(n).limit_denominator() for n in k]
    mult = np.lcm.reduce([f.denominator for f in frac])
    ints = [round(f*mult) for f in frac]
    lcm = np.lcm.reduce(ints)/mult # least common multiple of k
    l = [m*i for m in frac] # dipole lengths [nm]
    t2 = [t/2 for t in l] # thickness of the cell walls [nm]
    c2 = [t*q for t in t2] # cell sides [nm]
    s0 = lcm*max(c2)/max(k) # least common multiple of c2
    s2 = max(round(s/s0), 1)*s0 # shape side [nm]
    # instantiation arguments
    t = []
    # RDD
    t.append(('square', s, models.RDD, {'d': d}, 'edge', b))
    # RRDD
    for pv in ('E', 'R'):
        for ps in c:
            r = {'d': d, 'v': pv, 's': ps}
            t.append(('square', s, models.RRDD, r, 'edge', b))
    # RCDD
    for pv in ('E', 'R'):
        r = {'d': d, 'v': pv, 's': c1, 't': t1}
        t.append(('square', s1, models.RCDD, r, 'edge', b))
    for i in range(len(k)):
        r = {'d': d, 'v': 'D', 's': c2[i], 't': t2[i], 'l': l[i]}
        t.append(('square', s2, models.RCDD, r, 'edge', b))
    return t

if __name__ == "__main__":

    print("[SETTINGS]")

    for i in range(len(densities_m)):
        print("\nDensity of "+notation.quantity(densities_m[i], "nm^-2")+":")
        for args in arguments(densities[i]):
                print((args[0]
                    + " "+str(round(args[1]))+"nm"
                    + " "+args[4]
                    + " "+args[5]
                    + " "+args[2].__name__+notation.parameters(args[3])
                ))

    input("\nPress 'enter' to exit...")
